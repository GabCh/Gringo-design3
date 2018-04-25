import struct
from threading import Thread as th
from time import sleep

import numpy as np
import serial

from atlas.infrastructure.yaml_config_loader import ApplicationProperties

DEF_PWM_MAXPULSE = 4200


class ReceiveParser:
    def __init__(self, ctlobj):
        self.speed_log_old = None
        self.pos_log_old = None
        self.ctlobj = ctlobj

        self.ident_speed_file = open("speed.txt", "w")
        self.ident_pos_file = open("position.txt", "w")
        return

    def __del__(self):
        self.ident_speed_file.close()
        self.ident_pos_file.close()
        return

    def parse(self, stream):
        slen = 0
        while len(stream):
            op = stream[0]
            pk = None
            if op == 0x1E:
                ss = "=B4iI"
                slen = struct.calcsize(ss)
                pk = struct.unpack_from(ss, stream)
                self.cmd_pos_ident(pk)
            elif op == 0x1F:
                ss = "=B4hI"
                slen = struct.calcsize(ss)
                pk = struct.unpack_from(ss, stream)
                self.cmd_speed_ident(pk)
            elif op == 0x2A:
                slen = stream[1]
                ss = "=BB%ds" % (slen - 2)
                pk = struct.unpack_from(ss, stream)
                self.cmd_echo(pk)
            else:
                stream = stream[1:]
            stream = stream[slen:]

    def cmd_speed_ident(self, pk):
        self.speed_log_old = pk
        clk = pk[-1]
        res = pk[1:5]
        self.ctlobj.ident_res_spd += [[*res, clk]]
        self.ident_speed_file.write("%d, %d, %d, %d, %u\n" % (*res, clk))

    def cmd_pos_ident(self, pk):
        self.pos_log_old = pk
        clk = pk[-1]
        res = pk[1:5]
        self.ctlobj.ident_res_pos += [[*res, clk]]
        self.ident_pos_file.write("%d, %d, %d, %d, %u\n" % (*res, clk))

    def cmd_echo(self, pk):
        print("echo     -> \"%s\"" % pk[2:][0].decode('utf-8'))


class StmUsbCtl:
    def __init__(self, applicationProperties: ApplicationProperties):
        baudrate = 921600
        port = applicationProperties['stmctl']['port']
        self.m_ser = serial.Serial(port=port, baudrate=baudrate, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                   stopbits=serial.STOPBITS_ONE)
        self.m_cursorPos = 0
        self.m_stopRecv = 0

        self.ident_res_pos = []
        self.ident_res_spd = []

        self.recv_th = th(target=self.receive_thread, args=[])
        self.rp = ReceiveParser(self)

        self.pwm_maxpulse = DEF_PWM_MAXPULSE

    def __del__(self):
        self.m_ser.close()

    def echo(self, msg_str):
        msg = [ord(i) for i in msg_str]
        l = len(msg)
        if l > 62:
            return False
        packet = [0x2A, l + 2, *msg]
        self.m_ser.write(packet)
        return True

    def reset_speedpos(self):
        packet = struct.pack('=B', 0xE1)
        self.m_ser.write(packet)

    def set_pwm(self, motor_list, duty):
        mtr_flags = self.get_mflags(motor_list)
        duty_pulse = int(self.pwm_maxpulse * duty)
        packet = struct.pack('=BBH', 0xA1, mtr_flags, duty_pulse)
        self.m_ser.write(packet)

    def set_dir(self, motor_list, dir):
        mtr_flags = self.get_mflags(motor_list)
        packet = struct.pack('=BBb', 0xA2, mtr_flags, dir)
        self.m_ser.write(packet)

    def brake(self, motor_list):
        mtr_flags = self.get_mflags(motor_list)
        packet = struct.pack('=BB', 0xB4, mtr_flags)
        self.m_ser.write(packet)

    def get_mflags(self, mtr_dta):
        flags = 0
        if isinstance(mtr_dta, (list, tuple)):
            for i in mtr_dta:
                flags |= 2 ** i
        else:
            flags = mtr_dta
        return flags

    def receive_thread(self):
        while True:
            data = self.read()
            if data != None:
                self.rp.parse(data)
            if self.m_stopRecv:
                break
            sleep(0.1)

    def recv_start(self):
        self.recv_th.start()

    def recv_stop(self):
        self.m_stopRecv = 1

    def join_recvthread(self):
        self.recv_th.join()

    def read(self, bytecount=None):
        data = None
        bytecount = bytecount if bytecount != None else self.m_ser.in_waiting
        if bytecount:
            data = self.m_ser.read(bytecount)
        return data

    def enc_report_cfg(self, rate_spd, rate_pos):
        packet = struct.pack('=BHH', 0x1A, rate_spd, rate_pos)
        self.m_ser.write(packet)

    def enc_report_enable(self, spd, pos):
        packet = struct.pack('=BB', 0x1B, (pos << 1) | spd)
        self.m_ser.write(packet)

    def set_pwm_freq(self, freq):
        self.pwm_maxpulse = int(168000000 / freq)
        packet = struct.pack('=BI', 0xE2, freq)
        self.m_ser.write(packet)

    def set_enc_sampling(self, rate_spd, rate_pos):
        packet = struct.pack('=BHH', 0xE3, rate_spd, rate_pos)
        self.m_ser.write(packet)

    def ident_begin(self):
        packet = struct.pack('=B', 0xE4)
        self.m_ser.write(packet)

    def ident_end(self):
        packet = struct.pack('=B', 0xE5)
        self.m_ser.write(packet)

    def spdctl_setspeed(self, motor_list, speed):
        mtr_flags = self.get_mflags(motor_list)
        packet = struct.pack('=BBh', 0xB2, mtr_flags, speed)
        self.m_ser.write(packet)

    def start_ident(self, motor_list, steps, times):
        mtr_flags = self.get_mflags(motor_list)
        times = np.array(times) * 1000000
        steps = [int(i) for i in np.array(steps)]
        packet = struct.pack('=BB2h2I', 0x3A, mtr_flags, *steps, *times)
        self.m_ser.write(packet)

    def set_xpos_synced(self, dst):
        packet = struct.pack('=Bi', 0xC5, dst)
        self.m_ser.write(packet)

    def set_ypos_synced(self, dst):
        packet = struct.pack('=Bi', 0xC6, dst)
        self.m_ser.write(packet)

    def set_position_multi(self, motor_list, pos_array):
        mtr_flags = self.get_mflags(motor_list)
        packet = struct.pack('=BB4i', 0xC4, mtr_flags, *pos_array)
        self.m_ser.write(packet)

    def motor_rotate(self, deltapos):
        packet = struct.pack('=Bi', 0xC7, deltapos)
        self.m_ser.write(packet)

    def prehensor_ctl(self, lift=0):
        packet = struct.pack('=BB', 0x81, lift)
        self.m_ser.write(packet)
    def led_control(self, on=0):
        packet = struct.pack('=BB', 0x2D, on)
        self.m_ser.write(packet)

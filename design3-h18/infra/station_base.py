import argparse
import base64
import subprocess
import threading
import time
from datetime import datetime
from os import listdir, path
from os.path import isfile, join

import cv2
import requests
import sys
from flask import Flask, Response

parser = argparse.ArgumentParser(description="station base")
parser.add_argument("--camera", help="camera file [default: /dev/video0]", dest='camera', default="/dev/video0",
                    type=str)
parser.add_argument("--url", help="URL to server [default: http://design-whitecat.local:8080]",
                    dest='url', default="http://design-whitecat.local:8080", type=str)
args = parser.parse_args()

ROBOT_PC_URL = args.url
if not ROBOT_PC_URL.startswith("http://"):
    ROBOT_PC_URL = "http://" + ROBOT_PC_URL
if ROBOT_PC_URL.endswith("/"):
    ROBOT_PC_URL = ROBOT_PC_URL.rstrip("/")


def set_camera_settings(camera_file: str):
    subprocess.call(["uvcdynctrl", "-L", "cameraMondeSettings.txt", "-d", camera_file])


class CameraUSB:
    def __init__(self, source: str):
        self.capture = cv2.VideoCapture(source)
        if not self.capture.isOpened():
            # retry once
            time.sleep(1)
            self.capture = cv2.VideoCapture(source)

            if not self.capture.isOpened():
                raise RuntimeError('Could not start camera.')

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.get_frame()
        try:
            set_camera_settings(source)
        except:
            print('camera settings could not be set')

    def __del__(self):
        self.capture.release()

    def get_frame_bytes(self):
        _, img = self.capture.read()
        jpeg = cv2.imencode('.jpg', img)[1]
        return jpeg.tobytes()

    def get_frame(self):
        # self.capture.grab()
        is_frame_returned, frame = self.capture.read()
        return frame


class CameraLocalRepository:
    def __init__(self):
        self.directory = "training_datasets/blocks"
        self.files = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
        self.current_file = path.basename(self.files[0])
        self.files.sort()

    def get_frame_bytes(self):
        next_file = self.files.pop()
        file_name = join(self.directory, next_file)
        self.current_file = path.basename(file_name)
        img = cv2.imread(file_name)
        jpeg = cv2.imencode('.jpg', img)[1]
        return jpeg.tobytes()


if __name__ == '__main__':
    app = Flask(__name__)

    camera = CameraUSB(args.camera)


    def gen(cam):
        while True:
            frame = cam.get_frame_bytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


    def send_image(cam):
        buffer = cam.get_frame_bytes()
        b64 = base64.b64encode(buffer)
        string = b64.decode("utf-8")
        tag = "data:image/jpeg;base64,{0}".format(string)
        return tag


    @app.route('/video_feed')
    def video_feed():
        return Response(gen(camera),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


    @app.route('/video_feed/test')
    def test_video_feed():
        return Response(gen(CameraLocalRepository()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


    def update_image_mini_pc():
        while True:
            try:
                requests.post(ROBOT_PC_URL + "/image",
                              json={"image": str(base64.b64encode(camera.get_frame()))},
                              headers={'token': '07624953d862ede4a6264c42b3e81051'})
                print(datetime.now())
            except Exception:
                # Ignored
                pass


    threading.Thread(target=update_image_mini_pc).start()

    app.run(host='localhost', port=5000, threaded=True)

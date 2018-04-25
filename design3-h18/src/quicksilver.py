from flask import Flask, request
from flask.json import jsonify

from atlas.context.binder_config import StmRobotMotorControlBinder
from atlas.game.cube_grab_control import CubeGrabControl
from atlas.game.ir_code_reader import IrCodeReader
from atlas.game.led_control import LedControl
from atlas.infrastructure.binder import AbstractContext
from atlas.infrastructure.context import ApplicationContext
from atlas.motor.motor_control import MotorControl


@ApplicationContext
class QuickSilverContext(AbstractContext):

    def configure_service_locator(self):
        StmRobotMotorControlBinder().bind(self.serviceLocator)

    def yaml_config_filename(self) -> str:
        return "~/.atlas/debug.yml"


context = QuickSilverContext()
service_locator = context.service_locator()
app = Flask(__name__)


@app.route("/motor/forward", methods=['POST'])
def move_forward():
    content = request.get_json(force=True)
    distance = content['distance']
    service_locator.get(MotorControl).move_forward(distance)
    return "{}"


@app.route("/motor/left", methods=['POST'])
def move_left():
    content = request.get_json(force=True)
    distance = content['distance']
    service_locator.get(MotorControl).move_left(distance)
    return "{}"


@app.route("/motor/diagonal", methods=['POST'])
def move_diagonal():
    content = request.get_json(force=True)
    forward_distance = content['forward']
    left_distance = content['left']
    service_locator.get(MotorControl).move_diagonal(forward_distance, left_distance)
    return "{}"


@app.route("/motor/rotate", methods=['POST'])
def rotate():
    content = request.get_json(force=True)
    angle = content['angle']
    service_locator.get(MotorControl).rotate(angle)
    return "{}"


@app.route("/ir", methods=['GET'])
def get_ir():
    ir_code = service_locator.get(IrCodeReader).get_ir_code()
    return jsonify({"ir": ir_code})


@app.route("/grab", methods=['POST'])
def grab():
    service_locator.get(CubeGrabControl).grab()
    return "{}"


@app.route("/release", methods=['POST'])
def release():
    service_locator.get(CubeGrabControl).release()
    return "{}"


@app.route("/led/on", methods=['POST'])
def led_on():
    service_locator.get(LedControl).turn_on()
    return "{}"


@app.route("/led/off", methods=['POST'])
def led_off():
    service_locator.get(LedControl).turn_off()
    return "{}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

import base64
import time
from flask_socketio import SocketIO
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

from atlas.game.TaskFactory import TaskFactory
from atlas.game.TaskScheduler import TaskScheduler
from atlas.server.app.remote_web_image_repository import RemoteWebImageRepository

socket_io = SocketIO(async_mode='threading')


def create_app(task_scheduler: TaskScheduler, task_factory: TaskFactory,
               image_repository: RemoteWebImageRepository) -> Flask:
    from atlas.server.app.RouteHandler import RouteHandler

    app = Flask(__name__, instance_relative_config=True)

    socket_io.init_app(app)
    CORS(app)

    route_handler = RouteHandler(task_scheduler, task_factory, socket_io)

    @app.route('/tasks', methods=['POST'])
    def tasks():
        return route_handler.task()

    @app.route('/status', methods=['GET'])
    def get_status():
        return route_handler.game_status()

    @app.route('/image', methods=['POST'])
    def post_image():
        image_repository.set_image_from_base64_numpy_array(request.get_json()['image'])
        return make_response(jsonify({'message': 'ok'}), 200)

    @socket_io.on('tasks')
    def tasks(body):
        return route_handler.task()

    @app.errorhandler(401)
    def unauthorized(error):
        return route_handler.error_401()

    @app.errorhandler(500)
    def unauthorized(error):
        return route_handler.error_500()

    @app.route('/imageRequest', methods=['POST'])
    def trigger_image_request():
        socket_io.emit('image_request')
        t0 = time.time()
        return str(t0)

    @socket_io.on('image_receive')
    def image_receive(image_data):
        image_repository.add_image(image_data)

    return app

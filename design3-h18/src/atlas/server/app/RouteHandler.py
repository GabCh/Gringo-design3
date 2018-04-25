import json

from flask_socketio import SocketIO
from jsonschema import validate, ValidationError
from flask import abort, jsonify, make_response, request
from atlas.game.TaskFactory import TaskFactory
from atlas.game.TaskScheduler import TaskScheduler
from atlas.game.game_status import GameStatus
from atlas.infrastructure.binder import AbstractContext

TASKS_SCHEMA = {
    "type": "object",
    "required": [
        "tasks"
    ],
    "properties": {
        "tasks": {
            "type": "array",
            "items": {
                "required": [
                    "task_name",
                    "params"
                ],
                "type": "object",
                "properties": {
                    "task_name": {
                        "type": "string"
                    },
                    "params": {
                        "type": "object"
                    }
                },
                "additionalProperties": False
            }
        }
    },
    "additionalProperties": False
}


class RouteHandler(object):

    def __init__(self, task_scheduler: TaskScheduler, task_factory: TaskFactory, socket_io: SocketIO):
        self.task_scheduler = task_scheduler
        self.task_factory = task_factory
        self.socket_io = socket_io

    def _is_authenticated(self, headers):

        if 'token' not in headers:
            abort(401)
        else:
            token = headers['token']
            if not self._valid_credential(token):
                abort(401)

    @staticmethod
    def _valid_credential(token: str) -> bool:
        secret_token = '07624953d862ede4a6264c42b3e81051'
        return token == secret_token

    @staticmethod
    def _validate_task(data):
        data = json.loads(data)
        try:
            validate(data, TASKS_SCHEMA)
        except ValidationError:
            abort(400)

    def task(self):
        headers = request.headers
        data = request.data
        self._is_authenticated(headers)
        self._validate_task(data)
        data = json.loads(data)
        tasks = data['tasks']

        for serialize_task in tasks:
            task_name = serialize_task['task_name']
            task_params = serialize_task['params']
            task = self.task_factory.create_task(task_name, **task_params)
            self.task_scheduler.add_task(task)

        return make_response(jsonify({'message': 'ok'}), 200)

    def game_status(self):
        headers = request.headers
        self._is_authenticated(headers)

        service_locator = AbstractContext.INSTANCE.service_locator()
        game_status = service_locator.get(GameStatus)

        return make_response(game_status.to_json(), 200)

    @staticmethod
    def error_400():
        return make_response(jsonify({'error': 'Bad request.'}), 400)

    @staticmethod
    def error_401():
        return make_response(jsonify({'error': 'Wrong token.'}), 401)

    @staticmethod
    def error_500():
        return make_response(jsonify({'error': 'Internal server error.'}), 500)

import json

import requests
import sys

import time

if len(sys.argv) < 2:
    print("python task_helper.py localhost:8080")
BASE_URL = "http://" + sys.argv[1]


def doRequest(method: str, path: str, body=None):
    if body is None:
        body = {}
    headers = {
        'token': "07624953d862ede4a6264c42b3e81051",
        'cache-control': "no-cache"
    }

    return requests.request(method, BASE_URL + path, data=json.dumps(body), headers=headers)


while True:
    doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "update_board",
                "params": {
                }
            }
        ]
    })
    time.sleep(1)

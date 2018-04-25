import json
import sys

import requests

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


commands = [
    ("update board", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "update_board",
                "params": {
                }
            }

        ]
    })),
    ("status", lambda: doRequest("GET", "/status")),
    ("rotate by 10 degrees", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "rotate",
                "params": {
                    "angle": 10
                }
            }

        ]
    })),
    ("advance 5 cm", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "move_forward",
                "params": {
                    "distance": 0.05
                }
            }

        ]
    })),
    ("strafe left 5 cm", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "move_left",
                "params": {
                    "distance": 0.05
                }
            }

        ]
    })),
    ("goto (0.5,0.5)", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "goto",
                "params": {
                    "x": 0.5,
                    "y": 0.5,
                    "angle": 0
                }
            }

        ]
    })),
    ("set Canadian Flag (#34) as objective", lambda: doRequest("POST", "/tasks",
                                                               {
                                                                   "tasks": [
                                                                       {
                                                                           "task_name": "set_flag",
                                                                           "params": {
                                                                               "flag_code": 34
                                                                           }
                                                                       }

                                                                   ]
                                                               }
                                                               )),
    ("say hello 5 times", lambda: doRequest("POST", "/tasks",
                                            {
                                                "tasks": [
                                                    {
                                                        "task_name": "hello_task",
                                                        "params": {
                                                            "times": 5,
                                                            "interval": 1
                                                        }
                                                    }

                                                ]
                                            }
                                            )),
    ("grab the block", lambda: doRequest("POST", "/tasks",
                                         {
                                             "tasks": [
                                                 {
                                                     "task_name": "grab",
                                                     "params": {
                                                     }
                                                 }

                                             ]
                                         }
                                         )),
    ("release the block", lambda: doRequest("POST", "/tasks",
                                            {
                                                "tasks": [
                                                    {
                                                        "task_name": "release",
                                                        "params": {
                                                        }
                                                    }

                                                ]
                                            }
                                            )),
    ("get the ir code", lambda: doRequest("POST", "/tasks",
                                          {
                                              "tasks": [
                                                  {
                                                      "task_name": "get_ir",
                                                      "params": {
                                                      }
                                                  }

                                              ]
                                          }
                                          )),
    ("rotate by 120 degrees", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "rotate",
                "params": {
                    "angle": 120
                }
            }

        ]
    })),
    ("rotate by 360 degrees", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "rotate",
                "params": {
                    "angle": 360
                }
            }

        ]
    })),
    ("rotate by 45 degrees", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "rotate",
                "params": {
                    "angle": 45
                }
            }

        ]
    })),
    ("orient to north", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "orient_to",
                "params": {
                    "angle": 90
                }
            }

        ]
    })),
    ("orient to 43 degrees", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "orient_to",
                "params": {
                    "angle": 43
                }
            }

        ]
    })),
    ("orient to 223 degrees", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "orient_to",
                "params": {
                    "angle": 223
                }
            }

        ]
    })),
    ("fetch red block, drop at (0.5,0.5)", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "fetch",
                "params": {
                    "colour": 0,
                    "x": 0.5,
                    "y": 0.5
                }
            }
        ]
    })),
    ("realign to (0.5, 0.5)", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "realign",
                "params": {
                    "x": 0.5,
                    "y": 0.5
                }
            }
        ]
    })),
    ("start competition", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "start_competition",
                "params": {
                }
            }
        ]
    })),
    ("set Columbia (#40) as objective", lambda: doRequest("POST", "/tasks",
                                                          {
                                                              "tasks": [
                                                                  {
                                                                      "task_name": "set_flag",
                                                                      "params": {
                                                                          "flag_code": 40
                                                                      }
                                                                  }

                                                              ]
                                                          }
                                                          )),
    ("fetch blue block, drop at (0.5,0.5)", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "fetch",
                "params": {
                    "colour": 2,
                    "x": 0.5,
                    "y": 0.5
                }
            }
        ]
    })),
    ("led on", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "led_on",
                "params": {
                }
            }
        ]
    })),
    ("led off", lambda: doRequest("POST", "/tasks", {
        "tasks": [
            {
                "task_name": "led_off",
                "params": {
                }
            }
        ]
    })),

]


def printCommands():
    for i, command in enumerate(commands):
        print(i, ":", command[0])


while True:
    printCommands()
    command = input("Command number:")
    print(commands[int(command)][1]().json())

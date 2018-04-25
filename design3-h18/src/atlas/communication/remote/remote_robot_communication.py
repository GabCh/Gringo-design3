import json

import requests

from atlas.infrastructure.yaml_config_loader import ApplicationProperties


class RemoteRobotCommunication(object):

    def __init__(self, application_properties: ApplicationProperties):
        self.serverUrl = application_properties['remote']['robot_url']

    def doRequest(self, method: str, path: str, body=None):
        if body is None:
            body = {}
        headers = {
            'token': "07624953d862ede4a6264c42b3e81051",
            'cache-control': "no-cache"
        }

        return requests.request(method, self.serverUrl + path, data=json.dumps(body), headers=headers)

import json
import requests


class OnionRedisHTTPCall:

    def __init__(self, uri):
        self.uri = uri

    def consume(self, namespace, class_name, method_name, arguments):
        uri = "%s/%s/%s/%s" % (self.uri, namespace, class_name, method_name)
        response = requests.post(uri, json.dumps(arguments), headers={"Content-type": "application/json"})
        response = json.loads(response.text)
        return response

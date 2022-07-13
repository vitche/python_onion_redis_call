import json
import requests


class OnionRedisHTTPCall:

    def __init__(self, uri):
        self.uri = uri

    def consume(self, namespace, class_name, method_name, arguments):
        uri = "%s/%s/%s/%s" % (self.uri, namespace, class_name, method_name)
        response = requests.post(uri, json.dumps(arguments), headers={"Content-type": "application/json"})
        response = response.text
        response = json.loads(response)
        # A tricky way to parse the JSON string encoded twice in Onion Redis
        if isinstance(response, str):
          response = json.loads(response)
        return response

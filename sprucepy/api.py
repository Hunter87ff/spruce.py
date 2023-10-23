import os
import requests as req
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Sprucepy(object):
    app_id = None
    auth_token = None
    endpoint = None

    def __init__(self, endpoint='https://dashboard.87-hunter.repl.co/api/query'):
        self.endpoint = endpoint

    def ask(self, query:str) -> str:
        _resp = req(endpoint+f"?q={query}")
        return _resp["a"]


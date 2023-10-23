import os
try:
    #from urllib import urlencode
    import requests as req
except ImportError:
    #from urllib.parse import urlencode
    os.system("pip install -r requirements.txt")


class Sprucepy(object):
    app_id = None
    auth_token = None
    endpoint = None

    def __init__(self, endpoint='https://dashboard.87-hunter.repl.co/api/query'):
        self.endpoint = endpoint

    def ask(self, query:str) -> str:
        _resp = req(self.endpoint+f"?q={query}")
        return _resp["a"]


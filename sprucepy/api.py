import os
import requests as req
class Spruce:
    def __init__(self):
        self.ednpoint = 'https://dashboard.87-hunter.repl.co/api/query'

    def ask(self, query:str):
            _resp = req.get('https://dashboard.87-hunter.repl.co/api/query'+f"?q={query}").json() 
            return _resp["a"]

import requests

def GetSoup(url, heders=None):
    from bs4 import BeautifulSoup
    r = requests.get(url, headers=heders)
    return BeautifulSoup(r.content, 'html.parser')

def GetJson(url, params=None):
    import json
    r = requests.get(url, params=params)
    return json.loads(r.content)
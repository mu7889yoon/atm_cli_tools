import requests
import os

def StoreWebmUrlAction(webm_url:str)-> None:
    params = {
        'webm_url': webm_url
    }
    r = requests.post(os.environ['GAS_WEBM_LOGS_API'], params=params)

import requests
import os

def CheckWebmUrlAction(url):
    params = {
        'webm_url': url
    }
    r = requests.get(os.environ['GAS_WEBM_LOGS_API'], params=params)
    # 重複している場合はTrueを返す
    if r.text == 'true':
        return True
    else:
        return False
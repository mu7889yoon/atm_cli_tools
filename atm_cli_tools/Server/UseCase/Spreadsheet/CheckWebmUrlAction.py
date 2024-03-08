import requests
import os

def CheckWebmUrlAction(url: str)-> bool:
    params = {
        'webm_url': url
    }
    r = requests.get('https://script.google.com/macros/s/AKfycbwCBsS4KZMR-d2R8Dg3YwsmYaUMiOjyX2DOTmTBZnzN4n_Hidf5e5EzjLJ9NnSnbwdg/exec', params=params)
    # r = requests.get(os.environ['GAS_WEBM_LOGS_API'], params=params)
    # 重複している場合はTrueを返す
    if r.text == 'true':
        return True
    else:
        return False
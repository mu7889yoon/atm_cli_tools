import requests
import os

def StoreWebmUrlAction(webm_url):
    params = {
        'webm_url': webm_url
    }
    r = requests.post('https://script.google.com/macros/s/AKfycbwCBsS4KZMR-d2R8Dg3YwsmYaUMiOjyX2DOTmTBZnzN4n_Hidf5e5EzjLJ9NnSnbwdg/exec', params=params)
    # r = requests.post(os.environ['GAS_WEBM_LOGS_API'], params=params)

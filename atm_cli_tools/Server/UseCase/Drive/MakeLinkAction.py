import requests
import os

def MakeLinkAction(dest_dir_url, file_url):
    params = {
        'dest_dir_id': dest_dir_url,
        'file_id': file_url,
    }
    r = requests.get(os.environ['GAS_MAKE_LINK_API'],params=params)

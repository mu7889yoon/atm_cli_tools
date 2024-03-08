import requests
import os

def MakeLinkAction(dest_dir_url: str, file_url: str)-> None:
    params = {
        'dest_dir_id': dest_dir_url,
        'file_id': file_url,
    }
    r = requests.get('https://script.google.com/macros/s/AKfycbxdVu5o25l6nz2uiEBw_XU5kTrv-VeGRlQUEV-wKlnxqZPIraGFFiouPj04Wuu2J3yi6Q/exec', params=params)
    # r = requests.get(os.environ['GAS_MAKE_LINK_API'],params=params)

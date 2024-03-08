from typing import Union
from atm_cli_tools.helper import *

def GetAniDbUrlAction(slug:str)-> Union[str, None]:
    query = {
        'include': 'resources',
    }
    json_data = GetJson('https://api.animethemes.moe/anime/'+slug, query)
    json_data = json_data['anime']['resources']
    for data in json_data:
        if data['site'] == 'aniDB':
            return data['link']
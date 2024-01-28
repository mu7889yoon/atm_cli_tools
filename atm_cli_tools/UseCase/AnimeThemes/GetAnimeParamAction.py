from atm_cli_tools.helper import *
from atm_cli_tools.UseCase.GetSlugAction import GetSlugAction

def GetAnimeParamAction(url: str) -> object:
    slug = GetSlugAction(url)
    query = {
        'include': 'resources',
    }
    json_data = GetJson('https://api.animethemes.moe/anime/' + slug, query)
    param = {
        'en_title': json_data['anime']['name'],
        'aDB_url': ''
    }
    for resource in json_data['anime']['resources']:
        if resource['site'] == 'aniDB':
            param['aDB_url'] = resource['link']
        
    print(param)
    return param
    
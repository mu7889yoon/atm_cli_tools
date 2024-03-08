from atm_cli_tools.helper import *

def GetAllAnimesUrlAction(year: str, season: str)-> list:
    query = {
        'filter[year]': year,
        'filter[season]': season,
        'page[size]' :100,
    }
    json_data = GetJson('https://api.animethemes.moe/anime', query)
    anime_urls = ['https://animethemes.moe/anime/' + anime['slug'] for anime in json_data['anime']]
    return anime_urls

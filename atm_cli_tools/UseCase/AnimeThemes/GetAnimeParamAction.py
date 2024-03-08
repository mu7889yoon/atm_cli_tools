from atm_cli_tools.helper import *
from atm_cli_tools.UseCase.GetSlugAction import GetSlugAction
from atm_cli_tools.Model.Anime import Anime

def GetAnimeParamAction(url: str) -> Anime:
    slug = GetSlugAction(url)
    anime = Anime(slug)
    query = {
        'include': 'resources,animethemes.animethemeentries.videos,animethemes.song',
    }

    json_data = GetJson('https://api.animethemes.moe/anime/' + slug, query)

    anime.en_title = json_data['anime']['name']
    anime.aDB = {
        'url': '',
        'jp_title': '',
        'themes': [],
    }
    anime.asg = {
        'url': '',
        'jp_title': '',
    }
    anime.themes = []
    
    for resource in json_data['anime']['resources']:
        if resource['site'] == 'aniDB':
            anime.aDB['url'] = resource['link']
            
    for theme in json_data['anime']['animethemes']:
        for entrie in theme['animethemeentries']:
            for video in entrie['videos']:
                type = theme['slug']
                if entrie['version'] != 1 and entrie['version'] != None:
                    type += 'v' + str(entrie['version'])
                if video['tags'] != "":
                    type += '-' + video['tags']
                anime.themes.append({
                    'name': theme['song']['title'],
                    'type': type,
                    'webm_url': video['link'],
                    'theme_url': 'https://animethemes.moe/anime/' + slug + '/' + type,
                })
                
    return anime
    
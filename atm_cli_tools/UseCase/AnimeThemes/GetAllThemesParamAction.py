from atm_cli_tools.helper import *

def GetAllThemesParamAction(slug):
    query = {
        'include': 'animethemes.animethemeentries.videos,animethemes.song',
    }
    json_data = GetJson('https://api.animethemes.moe/anime/'+slug, query)
    themes = []
    slug = json_data['anime']['slug']
    animethemes = json_data['anime']['animethemes']
    for theme in animethemes:
        for entrie in theme['animethemeentries']:
            for video in entrie['videos']:
                type = theme['slug']
                if entrie['version'] != None:
                    type += 'v' + str(entrie['version'])
                if video['tags'] != "":
                    type += '-' + video['tags']
                themes.append({
                    'name': theme['song']['title'],
                    'type': type,
                    'webm_url': video['link'],
                    'theme_url': 'https://animethemes.moe/anime/' + slug + '/' + type,
                })        
    return themes

from atm_cli_tools.helper import GetSoup
from atm_cli_tools.UseCase.Theme.FindSimilarIdAction import FindSimilarIdAction
from atm_cli_tools.UseCase.AniDB.GetJpSongnameAction import GetJpSongnameAction as GetJpSongnameFromAdbAction
from atm_cli_tools.UseCase.AniDB.GetAniGenUrlAction import GetAniGenUrlAction
from atm_cli_tools.UseCase.AnisonGeneration.GetJpTitleAction import GetJpTitleAction as GetJpSongnameFromAsgAction
from atm_cli_tools.UseCase.AnisonGeneration.GetArtistAction import GetArtistAction as GetArtistFromAsgAction
from atm_cli_tools.Model.Theme import Theme

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

def TranslateAction(en_name:str, themes: list, theme: Theme) -> Theme:
    theme.songname['atm'] = en_name
        
    ret = {
        'songname' : {
            'atm' : en_name,
            'aDB' : '',
            'asg' : '',
        },
        'artist' : '',
    }
    aDB_url = FindSimilarIdAction(en_name, themes)
    if aDB_url:
        soup = GetSoup(aDB_url, headers)
        ret['songname']['aDB'] = GetJpSongnameFromAdbAction(soup)
        asg_url = GetAniGenUrlAction(soup)
        if asg_url:
            soup = GetSoup(asg_url)
            ret['songname']['asg'] = GetJpSongnameFromAsgAction(soup)
            ret['artist'] = GetArtistFromAsgAction(soup)
            
    return ret
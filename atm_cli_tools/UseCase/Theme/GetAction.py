from atm_cli_tools.Model.Anime import Anime
from atm_cli_tools.Model.Theme import Theme
from atm_cli_tools.UseCase.Theme.FindSimilarIdAction import FindSimilarIdAction
from atm_cli_tools.helper import GetSoup
from atm_cli_tools.UseCase.AniDB.GetJpSongnameAction import GetJpSongnameAction as GetJpSongnameFromAdbAction
from atm_cli_tools.UseCase.AnisonGeneration.GetJpTitleAction import GetJpTitleAction as GetJpsongnameFromAsgAction
from atm_cli_tools.UseCase.AniDB.GetAniGenUrlAction import GetAniGenUrlAction
from atm_cli_tools.UseCase.AnisonGeneration.GetArtistAction import GetArtistAction as GetArtistFromAsgAction

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

def GetAction(theme: dict, Anime: Anime) -> Theme:
    themes = Theme(
        theme['type'],
        theme['theme_url'],
        theme['webm_url'],
    )
    themes.anime_title = {
        'atm': Anime.en_title,
        'aDB': Anime.aDB['jp_title'],
        'asg': Anime.asg['jp_title'],
    }

    aDB_url = FindSimilarIdAction(theme['name'], Anime.aDB['themes'])
    themes.name = {
        'atm': theme['name'],
        'aDB': '',
        'asg': '',
    }
    themes.artist = ''
    # エラー処理必要
    if aDB_url:
        soup = GetSoup(aDB_url, headers)
        themes.name['aDB'] = GetJpSongnameFromAdbAction(soup)
        asg_url = GetAniGenUrlAction(soup)
        if asg_url:
            soup = GetSoup(asg_url)
            themes.name['asg'] = GetJpsongnameFromAsgAction(soup)
            themes.artist = GetArtistFromAsgAction(soup)
            
    return themes
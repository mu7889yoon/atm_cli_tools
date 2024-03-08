from atm_cli_tools.UseCase.AnimeThemes.GetAnimeParamAction import GetAnimeParamAction
from atm_cli_tools.UseCase.AnimeThemes.GetAllThemesParamAction import GetAllThemesParamAction
from atm_cli_tools.UseCase.AniDB.GetAniGenUrlAction import GetAniGenUrlAction
from atm_cli_tools.UseCase.AniDB.GetThemesTableAction import GetThemesTableAction
from atm_cli_tools.UseCase.AniDB.GetJpTitleAction import GetJpTitleAction as GetJpTitleFromAdbAction
from atm_cli_tools.UseCase.AnisonGeneration.GetJpTitleAction import GetJpTitleAction as GetJpTitleFromAsgAction

from atm_cli_tools.Model.Anime import Anime
from atm_cli_tools.helper import GetSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

def GetAction(anime_url: str) -> Anime:
    anime = GetAnimeParamAction(anime_url) 

    if anime.aDB['url']:
        soup = GetSoup(anime.aDB['url'], headers)
        anime.asg['url'] = GetAniGenUrlAction(soup)
        anime.aDB['jp_title'] = GetJpTitleFromAdbAction(soup)
        anime.jp_title = anime.aDB['jp_title']
        anime.aDB['themes'] = GetThemesTableAction(soup)
        
    if anime.asg['url']:
        soup = GetSoup(anime.asg['url'])
        anime.asg['jp_title'] = GetJpTitleFromAsgAction(soup)
        anime.jp_title = anime.asg['jp_title']
        

    return anime
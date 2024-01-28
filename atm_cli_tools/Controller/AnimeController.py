from atm_cli_tools.helper import *
from atm_cli_tools.UseCase.GetSlugAction import GetSlugAction
from atm_cli_tools.UseCase.AnimeThemes.GetAniDbUrlAction import GetAniDbUrlAction
from atm_cli_tools.UseCase.AnimeThemes.GetEnTitleAction import GetEnTitleAction as GetEnTitleFromAtmAction
from atm_cli_tools.UseCase.AniDB.GetAniGenUrlAction import GetAniGenUrlAction
from atm_cli_tools.UseCase.AniDB.GetJpTitleAction import GetJpTitleAction as GetJpTitleFromAdbAction
from atm_cli_tools.UseCase.AniDB.GetThemesTableAction import GetThemesTableAction
from atm_cli_tools.UseCase.AnisonGeneration.GetJpTitleAction import GetJpTitleAction as GetJpTitleFromAsgAction
from atm_cli_tools.UseCase.AnimeThemes.GetAllThemesParamAction import GetAllThemesParamAction
from atm_cli_tools.UseCase.AnimeThemes.GetAnimeParamAction import GetAnimeParamAction
from atm_cli_tools.Model.Anime import Anime

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class AnimeControllerClass:
    def __init__(self, url):
        self.url = url
        self.slug = GetSlugAction(url)
        self.Anime = Anime(self.slug)
        
    def return_anime_class(self):
        self.fetch_params()
        return self.Anime
    
    def fetch_params(self):
        param = GetAnimeParamAction(self.url)
        aDB_url = param['aDB_url']
        self.Anime.en_title = param['en_title']
        self.Anime.jp_title = ''
        self.Anime.themes_table = ''
        print(aDB_url   )
        if aDB_url:
            soup = GetSoup(aDB_url, headers)
            asg_url = GetAniGenUrlAction(soup)
            self.Anime.jp_title = GetJpTitleFromAdbAction(soup)
            self.Anime.themes_table = GetThemesTableAction(soup)
            if asg_url:
                soup = GetSoup(asg_url)
                self.Anime.jp_title = GetJpTitleFromAsgAction(soup)
        
    def find_themes(self, slug: str):
        return GetAllThemesParamAction(slug)
              
    def downloads(self):
        from atm_cli_tools.Controller.ThemeController import ThemeControllerClass
        self.fetch_params()
        themes = self.find_themes(self.slug)
        for theme in themes:
            ThemeControllerClass(theme['theme_url'], self.Anime).store_params(theme)
from atm_cli_tools.Controller.AnimeController import AnimeControllerClass
from atm_cli_tools.helper import *
from atm_cli_tools.Server.UseCase.Spreadsheet.CheckWebmUrlAction import CheckWebmUrlAction
from atm_cli_tools.Server.UseCase.Drive.MakeDirAction import MakeDirAction

class AnimeControllerForServerClass(AnimeControllerClass):
    def __init__(self, slug, year, season, daily_folder_id):
        url = 'https://animethemes.moe/anime/' + slug
        super().__init__(url)
        self.slug = slug
        self.year = year
        self.season = season
        self.daily_folder_id = daily_folder_id
        
    def create_folder(self):
        MakeDirAction(self.year +'/'+ self.season, self.Anime.jp_title)
        return self.year +'/'+ self.season +'/'+ self.Anime.jp_title

    def check_webms(self):
        import time
        themes = []
        for theme in super().find_themes(self.slug):
            if CheckWebmUrlAction(theme['webm_url']) == False:
                themes.append(theme)
            time.sleep(0.2)
        return themes
    
    def downloads(self):
        from atm_cli_tools.Server.Controller.ThemeControllerServer import ThemeControllerForServerClass
        themes = self.check_webms()
        if themes:
            super().fetch_params()
            path = self.create_folder()
            for theme in themes:
                ThemeControllerForServerClass(theme['theme_url'], self.Anime, theme, path, self.daily_folder_id).download()
from atm_cli_tools.Controller.AnimeController import AnimeControllerClass
from atm_cli_tools.helper import *
from atm_cli_tools.Server.UseCase.Spreadsheet.CheckWebmUrlsAction import CheckWebmUrlsAction
from atm_cli_tools.Server.UseCase.Drive.MakeDirAction import MakeDirAction

class AnimeControllerForServerClass(AnimeControllerClass):
    def __init__(self, url:str, year:str, daily_folder_id: str)->None:
        super().__init__(url)
        self.year = year
        self.daily_folder_id = daily_folder_id
        
    def create_folder(self) -> str: 
        MakeDirAction(self.year, self.Anime.jp_title)
        return self.year +'/'+ self.Anime.jp_title

    def download_themes(self) -> None:
        from atm_cli_tools.Server.Controller.ThemeControllerServer import ThemeControllerForServerClass
        undownload_themes = CheckWebmUrlsAction(self.Anime.themes)
        if undownload_themes:
            path = self.create_folder()
            for theme in undownload_themes:
                ThemeControllerForServerClass(theme, self.Anime, path, self.daily_folder_id)
    
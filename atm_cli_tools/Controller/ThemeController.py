from atm_cli_tools.helper import *

from atm_cli_tools.Model.Anime import Anime

from atm_cli_tools.UseCase.Theme.DetermineFilenameAction import DetermineFilenameAction
from atm_cli_tools.UseCase.Theme.DownloadAction import DownloadAction
from atm_cli_tools.UseCase.Theme.GetAction import GetAction

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class ThemeControllerClass:
    def __init__(self, theme: dict, Anime: Anime)-> None:
        self.theme = GetAction(theme, Anime)
        self.filename = DetermineFilenameAction(
            self.theme.name,
            self.theme.anime_title,
            self.theme.type,
            self.theme.artist
        )
        print(self.filename)
        # DownloadAction(self.theme.webm_url, self.filename)
        
    def download(self)-> str:
        path = DownloadAction(self.theme.webm_url, self.filename)
        return path
        
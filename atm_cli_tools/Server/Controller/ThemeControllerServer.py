from atm_cli_tools.Controller.ThemeController import ThemeControllerClass
from atm_cli_tools.Server.UseCase.Theme.DownloadAction import DownloadAction
from atm_cli_tools.Server.UseCase.Spreadsheet.StoreWebmUrlAction import StoreWebmUrlAction
from atm_cli_tools.Server.UseCase.Drive.GetIdAction import GetIdAction
from atm_cli_tools.UseCase.Theme.GetAction import GetAction
from atm_cli_tools.Server.UseCase.Drive.MakeLinkAction import MakeLinkAction
from atm_cli_tools.UseCase.Theme.DetermineFilenameAction import DetermineFilenameAction

from atm_cli_tools.Model.Anime import Anime

class ThemeControllerForServerClass(ThemeControllerClass):
    def __init__(self, theme: dict, Anime: Anime, path: str, daily_folder_id: str):
        self.theme = GetAction(theme, Anime)
        self.filename = DetermineFilenameAction(
            self.theme.name,
            self.theme.anime_title,
            self.theme.type,
            self.theme.artist,
            '.mp4',
        )
        
        self.path = path
        self.daily_folder_id = daily_folder_id
        DownloadAction(self.path, self.theme.webm_url, self.filename)
        file_id = GetIdAction(self.path + '/' + self.filename, 15)
        StoreWebmUrlAction(self.theme.webm_url)
        MakeLinkAction(self.daily_folder_id, file_id)
        
    def download(self) -> None:
        DownloadAction(self.path, self.Theme.webm_url, self.filename)
        file_id = GetIdAction(self.path + '/' + self.Theme.filename, 15)
        StoreWebmUrlAction(self.Theme.webm_url)
        MakeLinkAction(self.daily_folder_id, file_id)
        # ディスコードに通知
    
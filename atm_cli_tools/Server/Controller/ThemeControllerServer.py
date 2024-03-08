from atm_cli_tools.Controller.ThemeController import ThemeControllerClass
from atm_cli_tools.Server.UseCase.Theme.DownloadAction import DownloadAction
from atm_cli_tools.Server.UseCase.Spreadsheet.StoreWebmUrlAction import StoreWebmUrlAction
from atm_cli_tools.Server.UseCase.Drive.GetIdAction import GetIdAction
from atm_cli_tools.Server.UseCase.Drive.MakeLinkAction import MakeLinkAction

from atm_cli_tools.Model.Anime import Anime

class ThemeControllerForServerClass(ThemeControllerClass):
    def __init__(self, theme: dict, Anime: Anime, path: str, daily_folder_id: str)->None:
        super().__init__(theme, Anime, '.mp4')
        
        self.path = path
        self.daily_folder_id = daily_folder_id
        
    def download(self) -> None:
        path = DownloadAction(self.path, self.theme.webm_url, self.filename)
        file_id = GetIdAction(path, 5.0)
        StoreWebmUrlAction(self.Theme.webm_url)
        MakeLinkAction(self.daily_folder_id, file_id)
    
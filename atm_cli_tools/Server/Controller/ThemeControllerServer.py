from atm_cli_tools.Controller.ThemeController import ThemeControllerClass
from atm_cli_tools.Server.UseCase.Theme.DetermineFilenameAction import DetermineFilenameAction
from atm_cli_tools.Server.UseCase.Theme.DownloadAction import DownloadAction
from atm_cli_tools.Server.UseCase.Spreadsheet.StoreWebmUrlAction import StoreWebmUrlAction
from atm_cli_tools.Server.UseCase.Drive.GetIdAction import GetIdAction
from atm_cli_tools.Server.UseCase.Drive.MakeLinkAction import MakeLinkAction

class ThemeControllerForServerClass(ThemeControllerClass):
    def __init__(self, url, Anime, param, path, daily_folder_id):
        super().__init__(url, Anime)
        super().set_param(param)
        self.path = path
        self.daily_folder_id = daily_folder_id
        
    def determine_filename(self):
        data = DetermineFilenameAction(self.Theme.jp_songname, 
                                                      self.Theme.en_songname,
                                                      self.Anime.jp_title,
                                                      self.Anime.en_title,
                                                      self.Theme.type,
                                                      self.Theme.artist,
                                                      '.mp4')
        self.Theme.filename = data['filename']
        self.Theme.needfix = data['errors']
        
    def download(self):
        super().translate_songname()
        self.determine_filename()
        print(self.Theme.filename)
        DownloadAction(self.path, self.Theme.webm_url, self.Theme.filename)
        self.post_process()
        
    def post_process(self):
        StoreWebmUrlAction(self.Theme.webm_url)
        self.Theme.file_id = GetIdAction(self.path + '/' + self.Theme.filename, 15)
        print(self.Theme.file_id)
        MakeLinkAction(self.daily_folder_id, self.Theme.file_id)
        # ディスコードに通知
        #
        # Google Driveのリンクを取得する。
        # 今日作業分のフォルダにショートカットを追加する。
        # スプレッドシートに記録する。
        pass
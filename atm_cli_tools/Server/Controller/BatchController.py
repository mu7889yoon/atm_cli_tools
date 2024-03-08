from atm_cli_tools.Controller.AnimeController import AnimeControllerClass
from atm_cli_tools.helper import *

from atm_cli_tools.Server.UseCase.AnimeThemes.GetAllAnimesUrlAction import GetAllAnimesUrlAction
from atm_cli_tools.Server.UseCase.Drive.MakeDirAction import MakeDirAction
from atm_cli_tools.Server.UseCase.Drive.GetIdAction import GetIdAction

class BatchControllerClass:
    def __init__(self, year, season):
        self.year = str(year)
        self.season = season
        MakeDirAction('', self.year)
        self.daily_folder_id = self.create_daily_folder()
        self.fetch_params()
        return exit()
    
    def create_daily_folder(self)-> str:
        import datetime
        date = datetime.date.today()        
        MakeDirAction('BOT/', str(date))
        return GetIdAction('BOT/' + str(date), 15.0)
    
    # 今日作業分のフォルダを作成し、通知モデルに追加する。
    def fetch_params(self):
        from atm_cli_tools.Server.Controller.AnimeControllerServer import AnimeControllerForServerClass
        anime_urls = GetAllAnimesUrlAction(self.year, self.season)
        for anime_url in anime_urls:
            AnimeControllerForServerClass(anime_url, self.year, self.daily_folder_id).download_themes()
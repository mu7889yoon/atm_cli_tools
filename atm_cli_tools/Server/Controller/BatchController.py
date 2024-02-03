from atm_cli_tools.Controller.AnimeController import AnimeControllerClass
from atm_cli_tools.helper import *

from atm_cli_tools.Server.UseCase.AnimeThemes.GetAllAnimesUrlAction import GetAllAnimesUrlAction
from atm_cli_tools.Server.UseCase.Drive.MakeDirAction import MakeDirAction
from atm_cli_tools.Server.UseCase.Drive.GetIdAction import GetIdAction

class BatchControllerClass:
    def __init__(self, year, season):
        self.year = str(year)
        self.season = season
        MakeDirAction(self.year, self.season)
        self.create_daily_folder()
        self.fetch_params()
    
    def create_daily_folder(self):
        import datetime
        date = datetime.date.today()        
        MakeDirAction('BOT/', str(date))
        self.daily_folder_id = GetIdAction('BOT/' + str(date))
        print(self.daily_folder_id)
        
    
    # 今日作業分のフォルダを作成し、通知モデルに追加する。
    def fetch_params(self):
        from atm_cli_tools.Server.Controller.AnimeControllerServer import AnimeControllerForServerClass
        anime_slugs = GetAllAnimesUrlAction(self.year, self.season)
        for anime_slug in anime_slugs:
            AnimeControllerForServerClass(anime_slug, self.year, self.season, self.daily_folder_id).downloads()
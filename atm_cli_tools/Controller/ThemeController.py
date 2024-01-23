from atm_cli_tools.helper import *
from atm_cli_tools.Model.Theme import Theme

from atm_cli_tools.UseCase.Theme.GetTypeAction import GetTypeAction
from atm_cli_tools.UseCase.ConvertUrlAction import ConvertUrlAction
from atm_cli_tools.UseCase.Theme.FindSimilarAction import FindSimilarAction
from atm_cli_tools.UseCase.AniDB.GetJpSongnameAction import GetJpSongnameAction as GetJpSongnameFromAdbAction
from atm_cli_tools.UseCase.AniDB.GetAniGenUrlAction import GetAniGenUrlAction
from atm_cli_tools.UseCase.AnisonGeneration.GetJpTitleAction import GetJpTitleAction as GetJpSongnameFromAsgAction
from atm_cli_tools.UseCase.AnisonGeneration.GetArtistAction import GetArtistAction as GetArtistFromAsgAction
from atm_cli_tools.UseCase.Theme.DetermineFilenameAction import DetermineFilenameAction
from atm_cli_tools.UseCase.Theme.DownloadAction import DownloadAction
from atm_cli_tools.UseCase.GetSlugAction import GetSlugAction
from atm_cli_tools.UseCase.AnimeThemes.GetThemeParamAction import GetThemeParamAction

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class ThemeControllerClass:
    def __init__(self, url, Anime = None):
        self.url = url
        if Anime == None:
            from atm_cli_tools.Controller.AnimeController import AnimeControllerClass
            atm_url = ConvertUrlAction(self.url)
            self.Anime = AnimeControllerClass(atm_url).return_anime_class()
        else: self.Anime = Anime
        self.Theme = Theme(self.url, self.Anime)
    
    def fetch_params(self):
        slug = GetSlugAction(self.url)
        type = GetTypeAction(self.url)
        params = GetThemeParamAction(slug, type)
        return self.store_params(params)
        
    def store_params(self, params):
        self.Theme.webm_url = params['webm_url']
        self.Theme.en_songname = params['name']
        self.Theme.type = params['type']
        return self.download()
        
    def translate_songname(self):
        self.Theme.jp_songname = ''
        self.Theme.artist = ''
        aDB_url = FindSimilarAction(self.Theme.en_songname, self.Anime.themes_table)
        if aDB_url:
            soup = GetSoup(aDB_url, headers)
            self.Theme.jp_songname = GetJpSongnameFromAdbAction(soup)
            asg_url = GetAniGenUrlAction(soup)
            if asg_url:
                soup = GetSoup(asg_url)
                self.Theme.jp_songname = GetJpSongnameFromAsgAction(soup)
                # beta feature
                self.Theme.artist = GetArtistFromAsgAction(soup)
                
                
        
    def determine_filename(self):
        self.Theme.filename = DetermineFilenameAction(self.Theme.jp_songname, 
                                                      self.Theme.en_songname,
                                                      self.Anime.jp_title,
                                                      self.Anime.en_title,
                                                      self.Theme.type,
                                                      self.Theme.artist)
        
        
    def download(self):
        self.translate_songname()   
        self.determine_filename()
        DownloadAction(self.Theme.webm_url, self.Theme.filename)
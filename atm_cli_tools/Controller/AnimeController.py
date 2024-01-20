from helper import *
from UseCase.GetSlugAction import GetSlugAction
from UseCase.Anime.AnimeThemes.GetParamAction import GetParamAction as GetAtmParamAction
from UseCase.Anime.AniDB.GetParamAction import GetParamAction as GetAdbParamAction
from UseCase.Anime.AnisonGeneration.GetJpTitleAction import GetJpTitleAction as GetAsgParamAction
from Model.Anime import Anime



class AnimeControllerClass:
    def __init__(self, url, slug):
        self.url = url
        self.slug = 'a'
        self.Anime = Anime(self.slug)
        
    def fetch_params(self):
        GetAtmParamAction(self.Anime)
        GetAdbParamAction(self.Anime)
       
        if self.Anime.asg_url != None:
            GetAsgParamAction(self.Anime)
            
    
            
            
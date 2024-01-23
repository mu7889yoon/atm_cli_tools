from atm_cli_tools.helper import *
from atm_cli_tools.UseCase.AnimeThemes.GetAllThemesParamAction import GetAllThemesParamAction

def GetThemeParamAction(slug, type):
    themes = GetAllThemesParamAction(slug)
    for theme in themes:
        if theme['type'] == type:
            return theme
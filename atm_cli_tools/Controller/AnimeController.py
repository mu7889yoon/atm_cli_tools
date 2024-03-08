from atm_cli_tools.helper import *
from atm_cli_tools.UseCase.Anime.GetAction import GetAction as GetAnimeAction
from atm_cli_tools.Model.Anime import Anime

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class AnimeControllerClass:
    def __init__(self, url: str) -> None:
        self.Anime = GetAnimeAction(url)
    
    def download_themes(self) -> None:
        from atm_cli_tools.Controller.ThemeController import ThemeControllerClass
        themes = self.Anime.themes
        for theme in themes:
            ThemeControllerClass(theme, self.Anime)

    def download_theme(self, theme_url: str) -> None:
        from atm_cli_tools.Controller.ThemeController import ThemeControllerClass
        themes = self.Anime.themes
        theme = [theme for theme in themes if theme['theme_url'] == theme_url][0]
        ThemeControllerClass(theme, self.Anime)

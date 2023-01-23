import re

class Theme_props:
    def __init__(self, theme_url):
        self.url = theme_url
        # 最後のスラッシュ以降を取得
        self.anime_url = theme_url[:theme_url.rfind('/')]

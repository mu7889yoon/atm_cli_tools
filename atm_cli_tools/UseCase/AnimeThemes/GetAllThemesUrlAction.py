import re

def GetAllThemesUrlAction(soup):
    theme_url_field = soup.find_all('a', href=re.compile(r'^/anime/'))
    theme_urls = []
    if theme_url_field:
        for url in theme_url_field:
            theme_urls.append('https://animethemes.moe' + url.get('href'))
        return theme_urls
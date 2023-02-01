import re
import requests
from bs4 import BeautifulSoup
import json
from lxml import html

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class Props:
    def __init__(self, theme_url):
        self.theme_url = theme_url
        anime_url = theme_url[:theme_url.rfind('/')]
        self.slug_anime_name = anime_url[anime_url.rfind('/')+1:]
        self.theme_soup  = BeautifulSoup(requests.get(self.theme_url, headers=headers).text, 'html.parser')
        self.webm_url = self.theme_soup.find('meta', content=re.compile('https://v.animethemes.moe/')).get('content')

    def renamer(self):
        self.en_theme_name = self.theme_soup.find('span', color='text-primary').text
        atm_api = requests.get('https://api.animethemes.moe/anime/'+self.slug_anime_name+'?include=resources')
        atm_api = atm_api.json()['anime']['resources']
        for i in atm_api:
            if i['site'] == 'aniDB':
                self.aDB_url = i['link']
                break
        print(self.aDB_url)
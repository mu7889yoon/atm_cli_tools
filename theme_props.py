import re
import requests
from bs4 import BeautifulSoup
import json
from lxml import html

class Props:
    def __init__(self, theme_url):
        self.theme_url = theme_url
        self.anime_url = theme_url[:theme_url.rfind('/')]

    def dump_web_page(self, url):
        r = requests.get(url)
        s = BeautifulSoup(r.text, 'html.parser')
        return s

    def download_webm(self):
        self.theme_soup = self.dump_web_page(self.theme_url)
        s = self.theme_soup
        self.webm_url = s.find('meta', attrs={'name':'og:video','content':re.compile(r'v\.animethemes\.moe')}).get('content')
        

    def rename(self):
        atm_theme_name = html.fromstring(str(self.theme_soup))
        atm_theme_name = atm_theme_name.xpath('/html/body/div/div[1]/div[2]/div[1]/div/span/span[1]/text()')
        print(atm_theme_name)
        
        


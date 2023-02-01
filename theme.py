import re
import requests
from bs4 import BeautifulSoup
import json
from lxml import html
import string
import difflib

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class Props:
    def __init__(self, theme_url):
        self.theme_url = theme_url
        anime_url = theme_url[:theme_url.rfind('/')]
        self.slug_anime_name = anime_url[anime_url.rfind('/')+1:]
        self.theme_soup  = BeautifulSoup(requests.get(self.theme_url, headers=headers).text, 'html.parser')
        self.webm_url = self.theme_soup.find('meta', content=re.compile('https://v.animethemes.moe/')).get('content')

    def renamer(self):
        anime_name = self.get_jp_anime_name()
        theme_name = self.get_jp_theme_name()
        theme_type = self.webm_url[self.webm_url.rfind('-')+1:self.webm_url.rfind('.')]
        self.file_name = anime_name + ' ' + theme_type + ' ' + theme_name + '.webm'

    def get_jp_anime_name(self):
        anime_url = self.theme_url[:self.theme_url.rfind('/')]
        slug_anime_name = anime_url[anime_url.rfind('/')+1:]
        atm_api = requests.get('https://api.animethemes.moe/anime/'+ slug_anime_name +'?include=resources')
        atm_api = atm_api.json()['anime']['resources']
        for i in atm_api:
            if i['site'] == 'aniDB':
                aDB_url = i['link']
                break
        self.aDB_soup = BeautifulSoup(requests.get(aDB_url, headers=headers).text, 'html.parser')
        aDB_jp_anime_name = self.aDB_soup.find('span', class_="i_icon i_flag i_audio_ja" ,title="language: japanese")
        if aDB_jp_anime_name != None:
            aDB_jp_anime_name = aDB_jp_anime_name.parent.parent.find('label',itemprop="alternateName").string
        else:
            aDB_jp_anime_name = None
        asg_url = self.aDB_soup.find('a',href=re.compile('anison.info/'))['href']
        if asg_url != None:
            asg_jp_anime_name = None
        else:
            asg_soup = BeautifulSoup(requests.get(asg_url, headers=headers).text, 'html.parser')
            asg_jp_anime_name = asg_soup.find('div', class_='subject').text
        if aDB_jp_anime_name == None and asg_jp_anime_name == None:
            print('No Japanese anime name found.')
            return slug_anime_name
        elif aDB_jp_anime_name == None:
            return asg_jp_anime_name
        elif asg_jp_anime_name == None:
            return aDB_jp_anime_name
        elif difflib.SequenceMatcher(None, aDB_jp_anime_name, asg_jp_anime_name).ratio() > 0.9:
            return aDB_jp_anime_name
        else:
            return asg_jp_anime_name
        
    # 曲名を英語から日本語に変換する
    def get_jp_theme_name(self):
        self.en_theme_name = self.theme_soup.find('span', color='text-primary').text
        self.themes_table =  self.aDB_soup.find_all('td', class_='name song')
        themes_list = []
        for i in self.themes_table:
            themes_list.append(i.find('a').text.upper())
        ret = difflib.get_close_matches(self.en_theme_name.upper(),themes_list,cutoff=0.85)
        aDB_theme_url = self.themes_table[themes_list.index(ret[0])].find('a')['href']
        aDB_theme_soup = BeautifulSoup(requests.get('https://anidb.net'+aDB_theme_url, headers=headers).text, 'html.parser')
        jp_theme_name = aDB_theme_soup.find('span', class_="i_icon i_flag i_audio_ja" ,title="language: japanese")
        if jp_theme_name!= None:
            return jp_theme_name.parent.parent.find('label',itemprop="alternateName").string
        else:
            print('No Japanese theme name found.')
            return self.en_theme_name
            



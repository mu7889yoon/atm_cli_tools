from bs4 import BeautifulSoup
import requests
import re

import help_error
import extractor
import renamer

def get_html(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    return s

def find_webm(soup):
    webm_url = soup.find('meta',content=re.compile(".webm$"))
    return webm_url['content']
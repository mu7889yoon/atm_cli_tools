import requests
import re
from bs4 import BeautifulSoup
import sys
from theme_props import Props as tp

args = sys.argv
url = args[1]

theme_props = tp(url)
print(theme_props.theme_url)
print(theme_props.anime_url)
theme_props.download_webm()
print(theme_props.webm_url)
theme_props.rename()

import requests
import re
from bs4 import BeautifulSoup

class Theme_props:
    def __init__(self, name, url):
        self.name = name
        self.url = url

import sys
import help_error
import requests
from bs4 import BeautifulSoup
import re
import difflib
import wget

import downloader
import extractor
import renamer

args = sys.argv
# Validate args
if len(args) < 2:
    help_error.error_exit('Error: No URL specified')
# --help or -h option
if args[1] == '--help' or args[1] == '-h':
    help_error.help()
# Validate URL
if not downloader.validate_url(args[1]):
    help_error.error_exit('Error: Invalid URL')
# Start downloading
downloader.download(args[1])




def get_atm_anime_page_url(OPED_url):
    return OPED_url[:OPED_url.rfind('/')]

def get_soup_from_url(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

def find_aDB_url_from_atm_anime_page_soup(soup):
    aDB_url = soup.find('a',href=re.compile('https://anidb.net/anime/'))
    return aDB_url['href']

def get_aDB_soup_from_aDB_url(aDB_url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    return BeautifulSoup(requests.get(aDB_url, headers=headers).text, 'html.parser')

def get_aDB_soup_from_atm_anime_page_url(Anime_page_url):
    anime_soup = get_soup_from_url(Anime_page_url)
    aDB_url = find_aDB_url_from_atm_anime_page_soup(anime_soup)
    aDB_soup = get_aDB_soup_from_aDB_url(aDB_url)
    return aDB_soup

def test_code():
    aDB_soup = BeautifulSoup(open('10288.html'), 'html.parser')
    return aDB_soup

def find_asg_url_from_aDB_soup(soup):
    asg_url = soup.find('a',href=re.compile('anison.info/'))
    return asg_url['href']

def get_jp_anime_title_from_asg_url(url):
    soup = get_soup_from_url(url)
    title = soup.find('div', class_='subject').text
    return title

def get_theme_type_from_OPED_url(OPED_url):
    type = OPED_url[OPED_url.rfind('/')+1:]
    if type.find('-') != -1:
        type = type[:type.find('-')]
    return type


def get_jp_anime_title_from_aDB_soup(soup):
    asg_url = find_asg_url_from_aDB_soup(soup)
    return get_jp_anime_title_from_asg_url(asg_url)

def get_song_table_from_aDB_soup(soup):
    return soup.find_all('td', class_='name song')

def get_song_name_from_OPED_soup(soup):
    song_name = soup.find('span', color='text-primary', class_='sc-320a02c8-0 blPzQM').text
    return song_name

def get_webm_url_from_OPED_soup(soup):
    webm_url = soup.find('meta', content=re.compile('https://v.animethemes.moe/')).get('content')
    return webm_url

def UPPER_to_case(song_names):
  song_names_Upper = []
  for song_name in song_names:
    song_names_Upper.append(song_name.upper())
  return song_names_Upper

def get_song_names_from_aDB_song_table(song_table):
    song_names = []
    for song in song_table:
        song_names.append(song.find('a').text)
    return song_names

def get_close_word_return_index_No(song_name,song_names_Upper):
  song_name_Upper = song_name.upper()
  ret = difflib.get_close_matches(song_name_Upper,song_names_Upper,cutoff=0.85)
  if ret:
    index_no = song_names_Upper.index(ret[0])
    return index_no
  elif not ret:
    return -1


def translate_song_name_to_jp(song_name,song_table):
    song_names = get_song_names_from_aDB_song_table(song_table)
    song_names_Upper = UPPER_to_case(song_names)
    index_no = get_close_word_return_index_No(song_name,song_names_Upper)
    if index_no == -1:
        return -1
    else:
        aDB_song_url = 'https://anidb.net'+song_table[index_no].find('a').get('href')
        aDB_song_soup = get_aDB_soup_from_aDB_url(aDB_song_url)
        song_name_jp = search_jp_song_title_from_aDB_soup(aDB_song_soup)
        return song_name_jp

def search_jp_song_title_from_aDB_soup(aDB_song_soup):
  jp_song_title = aDB_song_soup.find('span', class_="i_icon i_flag i_audio_ja" ,title="language: japanese")
  if jp_song_title != None:
    jp_song_title = jp_song_title.parent.parent.find('label',itemprop="alternateName").string
    return jp_song_title
  elif jp_song_title == None:
    return None

def determine_filename(OPED_url):
    atm_song_soup = get_soup_from_url(OPED_url)
    song_name = get_song_name_from_OPED_soup(atm_song_soup)
    webm_url = get_webm_url_from_OPED_soup(atm_song_soup)
    type = get_theme_type_from_OPED_url(OPED_url)
    Anime_url = get_atm_anime_page_url(OPED_url)
    atm_soup = get_soup_from_url(Anime_url)
    aDB_soup = get_aDB_soup_from_atm_anime_page_url(Anime_url)
    anime_title = get_jp_anime_title_from_aDB_soup(aDB_soup)
    song_table = get_song_table_from_aDB_soup(aDB_soup)
    song_name_jp = translate_song_name_to_jp(song_name,song_table)
    file_name = anime_title+' '+type+' '+song_name_jp+'.webm'
    return webm_url,file_name


def download_atm_theme(OPED_url):
    webm_url,file_name = determine_filename(OPED_url)
    wget.download(webm_url, file_name)


OPED_url = sys.argv[1]
download_atm_theme(OPED_url)

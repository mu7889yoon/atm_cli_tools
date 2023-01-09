import wget
# import multiprocessing

import help_error
import extractor
import renamer

def validate_url(url):
    if url.startswith('https://animethemes.moe/anime/'):
        return True
    else:
        return False

def download(url):
    print('Downloading...')
    soup = extractor.get_html(url)
    webm = extractor.find_webm(soup)
    # [ToDo] Multiprocessing
    filename = wget.filename(webm)
    wget.download(webm)
    renamer.rename(soup, filename)
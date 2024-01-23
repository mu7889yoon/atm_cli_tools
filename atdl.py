import argparse
from urllib.parse import urlparse
from atm_cli_tools.Validate.UrlRequest import UrlRequest
from atm_cli_tools.Controller.ThemeController import ThemeControllerClass
from atm_cli_tools.Controller.AnimeController import AnimeControllerClass
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL to be processed')
    args = parser.parse_args()
    url = args.url
    
    # url の末尾に / がある場合、削除する
    if url[-1] == '/': url = url[:-1]
    
    UrlRequest(url)
    depth = urlparse(url).path.count('/')
    if depth == 3:
        ThemeControllerClass(url).fetch_params()
    elif depth == 2:
        AnimeControllerClass(url).downloads()
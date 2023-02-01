import argparse
from theme import Props

parser = argparse.ArgumentParser()
parser.add_argument('url', help='URL of the theme page EX: https://animethemes.moe/anime/hayate_no_gotoku/OP2-BD1072')
# -f でオプションを指定する
parser.add_argument('-f', '--fast', help='Without rename, Just Download', action='store_true')
args = parser.parse_args()
url = args.url
option = '-f' if args.fast else None

props = Props(url, option)
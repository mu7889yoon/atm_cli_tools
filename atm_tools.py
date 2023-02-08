import argparse
from theme import Props
import os

parser = argparse.ArgumentParser()
parser.add_argument('url', help='URL of the theme page EX: https://animethemes.moe/anime/hayate_no_gotoku/OP2-BD1072')
parser.add_argument('-f', '--fast', help='Without rename, Just Download', action='store_true')
parser.add_argument('-o', '--output', help='Output file name')
args = parser.parse_args()
url = args.url
option = '-f' if args.fast else None
if args.output:
    os.chdir(args.output)
props = Props(url, option)
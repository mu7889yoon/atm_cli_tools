import argparse
from theme import Props
import os

parser = argparse.ArgumentParser()
parser.add_argument('url', help='URL of the theme page EX: https://animethemes.moe/anime/hayate_no_gotoku/OP2-BD1072', nargs='?')
parser.add_argument('-f', '--fast', help='Without rename, Just Download', action='store_true')
parser.add_argument('-d', '--dir', help='Directory to save the theme', default=os.getcwd())
args = parser.parse_args()
url = args.url
option = '-f' if args.fast else None
directory = args.dir
os.chdir(directory)
if url != None:
    props = Props(url, option)
elif url == None:
    print('Input Animethemes URL')
    while True:
        url = input('ATDL >> ')
        if url == 'exit':
            break
        props = Props(url, option)
        print('')

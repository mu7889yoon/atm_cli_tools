import sys

def error_exit(msg):
    print(msg)
    sys.exit(1)

def help():
    print('Usage: atdl [URL] <options>')
    print('URL: example  ex: https://animethemes.moe/anime/suzumiya_haruhi_no_yuuutsu/ED-NCBD1080')
    print('Options:')
    sys.exit(0)
    
import re

def FilenameRequest(filename):
    return re.sub(r'[\\/:*?"<>|]', ' ', filename)
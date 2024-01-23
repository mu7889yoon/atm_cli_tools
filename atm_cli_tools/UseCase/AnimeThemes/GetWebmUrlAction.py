import re

def GetWebmUrlAction(soup):
    return soup.find('meta', content=re.compile('https://v.animethemes.moe/')).get('content')
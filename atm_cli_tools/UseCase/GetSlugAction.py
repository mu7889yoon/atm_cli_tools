from urllib.parse import urlparse

def GetSlugAction(url):
    return urlparse(url).path.split('/')[2]
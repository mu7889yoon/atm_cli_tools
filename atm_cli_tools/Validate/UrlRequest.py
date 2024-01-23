from urllib.parse import urlparse

def UrlRequest(url):
    # url がプロトコルなしで与えられた場合、付与する
    if url.find('://') == -1: url = 'https://' + url  
        
    req = urlparse(url)
    if req.netloc != 'animethemes.moe' or not req.path.startswith('/anime/'):
        raise ValueError('Invalid URL')
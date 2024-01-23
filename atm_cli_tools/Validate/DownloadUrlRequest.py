from urllib.parse import urlparse

def DownloadUrlRequest(url):
    # url がプロトコルなしで与えられた場合、付与する
    if url.find('://') == -1: url = 'https://' + url  
        
    req = urlparse(url)
    if req.netloc != 'v.animethemes.moe' or not req.path.endswith('.webm'):
        raise ValueError('Invalid URL')
import requests

def DownloadAction(webm_url: str, filename: str)-> str:
    requests.get(webm_url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in requests.get(webm_url, stream=True).iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
                f.flush()         
            
    return filename
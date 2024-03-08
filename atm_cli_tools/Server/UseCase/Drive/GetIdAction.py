from kora.xattr import get_id
import time

def GetIdAction(path: str, wait: float = 0.5)-> str:
    time.sleep(wait)
    return get_id(path)
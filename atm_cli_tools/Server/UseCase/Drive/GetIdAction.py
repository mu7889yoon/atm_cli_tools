from kora.xattr import get_id
import time
def GetIdAction(path, wait=0.5):
    time.sleep(wait)
    return get_id(path)
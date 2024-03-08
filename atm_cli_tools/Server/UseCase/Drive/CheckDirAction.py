import os

def CheckDirAction(path: str, dir_name: str)-> bool:
    if os.path.exists(path + dir_name):
        return False
    return True
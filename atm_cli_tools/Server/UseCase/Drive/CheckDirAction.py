import os
def CheckDirAction(path, dir_name):
    if os.path.exists(path + dir_name):
        return False
    return True
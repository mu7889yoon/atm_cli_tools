import os
from atm_cli_tools.Validate.FilenameRequest import FilenameRequest

def MakeDirAction(path: str, dir_name: str)-> None:
    dir_name = FilenameRequest(dir_name)
    os.makedirs(path + '/' + dir_name, exist_ok=True)
    
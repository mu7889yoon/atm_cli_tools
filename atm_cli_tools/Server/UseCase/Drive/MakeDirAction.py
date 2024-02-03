import os
from atm_cli_tools.Server.UseCase.Drive.CheckDirAction import CheckDirAction

def MakeDirAction(path, dir_name):
    os.makedirs(path + '/' + dir_name, exist_ok=True)
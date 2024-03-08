import os
from atm_cli_tools.Server.UseCase.Drive.CheckDirAction import CheckDirAction
from atm_cli_tools.Validate.FilenameRequest import FilenameRequest

def MakeDirAction(path, dir_name):
    dir_name = FilenameRequest(dir_name)
    os.makedirs(path + '/' + dir_name, exist_ok=True)
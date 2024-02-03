from atm_cli_tools.Server.UseCase.Drive.GetIdAction import GetIdAction
def GetDirIdAction(path):
    id = GetIdAction(path)
    return f'https://drive.google.com/drive/folders/{id}'
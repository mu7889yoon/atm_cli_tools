from atm_cli_tools.Server.UseCase.Drive.GetIdAction import GetIdAction
def GetFileUrlAction(path):
    id = GetIdAction(path)
    return f'https://drive.google.com/file/d/{id}'
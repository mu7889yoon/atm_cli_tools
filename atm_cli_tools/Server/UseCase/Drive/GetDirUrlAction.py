from atm_cli_tools.Server.UseCase.Drive.GetIdAction import GetIdAction

def GetDirUrlAction(path: str)-> str:
    id = GetIdAction(path)
    return f'https://drive.google.com/drive/folders/{id}'
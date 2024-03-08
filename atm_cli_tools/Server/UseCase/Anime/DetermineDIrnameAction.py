from atm_cli_tools.Validate.FilenameRequest import FilenameRequest

def DetermineDIrnameAction(anime_titles:dict)-> str:
    def setprop(data:dict):
        if data['asg']:
            return data['asg']
        elif data['aDB']:
            return data['aDB']
        else:
            return data['atm']
    anime_title = setprop(anime_titles)
    anime_title = FilenameRequest(anime_title)
    return anime_title
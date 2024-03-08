from atm_cli_tools.Validate.FilenameRequest import FilenameRequest

def DetermineFilenameAction(
        names: dict,
        anime_titles: dict,
        theme_type: str,
        artist: str,
        extension: str = '.mp4'
    )-> object:

    def setprop(data:dict):
        if data['asg']:
            return data['asg']
        elif data['aDB']:
            return data['aDB']
        else:
            return data['atm']

    songname = setprop(names)
    anime_title = setprop(anime_titles)
    if artist:
        artist = ' ' + artist
    else:
        artist = ''
    filename = FilenameRequest(songname + ' ' + anime_title + ' ' + theme_type + artist + extension)

    return filename
    return {'filename': filename, 'errors': errors}
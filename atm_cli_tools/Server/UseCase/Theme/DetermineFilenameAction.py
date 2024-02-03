from atm_cli_tools.Validate.FilenameRequest import FilenameRequest

def DetermineFilenameAction(jp_songname, en_songname,
                            jp_title, en_title,
                            theme_type, jp_artist = None,
                            extension = '.webm'):
    errors = []
    if jp_songname:
        songname = jp_songname
    else:
        songname = en_songname
        errors.append({'has_err_songname': True})
    if jp_title:
        title = jp_title
    else:
        title = en_title
        errors.append({'has_err_title': True})
    if jp_artist:
        artist = ' ' + jp_artist
    else:
        artist = ''
        errors.append({'has_err_artist': True})
    
    filename = FilenameRequest(songname + ' ' + title + ' ' + theme_type + artist + extension)
    
    return {'filename': filename, 'errors': errors}
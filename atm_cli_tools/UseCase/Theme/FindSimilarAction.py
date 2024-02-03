import difflib

def FindSimilarAction(en_songname, themes):
    ret = difflib.get_close_matches(
        en_songname.upper(),
        [theme['songname'] for theme in themes],
        cutoff=0.85
    )
    if ret:
        id = themes[[theme['songname'] for theme in themes].index(ret[0])]['id']
        return 'https://anidb.net' + id
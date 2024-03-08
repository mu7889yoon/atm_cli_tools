import difflib
from typing import Union

def FindSimilarIdAction(en_songname: str, themes: list) -> Union[str, None]:
    ret = difflib.get_close_matches(
        en_songname.upper(),
        [theme['songname'] for theme in themes],
        cutoff=0.85
    )
    if ret:
        id = themes[[theme['songname'] for theme in themes].index(ret[0])]['id']
        return 'https://anidb.net' + id
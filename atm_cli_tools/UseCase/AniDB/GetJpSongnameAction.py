from typing import Union

def GetJpSongnameAction(soup: str) -> Union[str, None]:
    jp_songname_field = soup.find('span', class_="i_icon i_flag i_audio_ja" ,title="language: japanese")
    if jp_songname_field:
        return jp_songname_field.parent.parent.find('label',itemprop="alternateName").string
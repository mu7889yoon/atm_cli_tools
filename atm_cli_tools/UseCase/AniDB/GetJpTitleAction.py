from typing import Union
def GetJpTitleAction(soup: str) -> Union[str, None]:
    jp_title_field = soup.find('span', class_="i_icon i_flag i_audio_ja" ,title="language: japanese")
    if jp_title_field:
        return jp_title_field.parent.parent.find('label',itemprop="alternateName").string
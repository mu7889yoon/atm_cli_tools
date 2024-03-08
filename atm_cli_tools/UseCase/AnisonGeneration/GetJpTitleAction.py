from typing import Union

def GetJpTitleAction(soup: str) -> Union[str, None]:
    jp_title_field = soup.find('div', class_="subject")
    if jp_title_field:
        return jp_title_field.text
from typing import Union

def GetAniGenUrlAction(soup: str) -> Union[str, None]:
    asg_url_field = soup.find('a', class_='i_icon i_resource_anison brand')
    if asg_url_field:
        return soup.find('a', class_='i_icon i_resource_anison brand').get('href')
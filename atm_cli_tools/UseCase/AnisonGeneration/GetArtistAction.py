from typing import Union

def GetArtistAction(soup:str)-> Union[str, None]:
    artist_field = soup.find('td', text='歌手').parent
    if artist_field:
        return artist_field.find('a').text
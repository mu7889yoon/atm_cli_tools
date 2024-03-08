from typing import List, Dict

def GetThemesTableAction(soup) -> List[Dict]:
    theme_table_field = soup.find('table', class_='songlist')
    if theme_table_field:
        rows = soup.find('table', class_='songlist').find_all('td', class_='name song')
        themes = []
        for row in rows:
            themes.append({
                    'songname': row.find('a').text.upper(),
                    'id': row.find('a')['href'],
            })       
        return themes
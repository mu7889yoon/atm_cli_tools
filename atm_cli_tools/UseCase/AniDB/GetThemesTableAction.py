def GetThemesTableAction(soup):
    if soup.find('table', class_='songlist') != None:
        rows = soup.find('table', class_='songlist').find_all('td', class_='name song')
        themes = []
        for row in rows:
            themes.append({
                    'songname': row.find('a').text.upper(),
                    'id': row.find('a')['href']
            })       
        return themes
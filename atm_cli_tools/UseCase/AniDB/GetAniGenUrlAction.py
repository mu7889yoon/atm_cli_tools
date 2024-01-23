def GetAniGenUrlAction(soup):
    if soup.find('a', class_='i_icon i_resource_anison brand') != None:
        return soup.find('a', class_='i_icon i_resource_anison brand').get('href')
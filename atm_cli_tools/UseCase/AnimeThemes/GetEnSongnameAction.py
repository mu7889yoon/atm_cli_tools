def GetEnSongnameAction(soup):
    return soup.find('span', color='text-primary').text
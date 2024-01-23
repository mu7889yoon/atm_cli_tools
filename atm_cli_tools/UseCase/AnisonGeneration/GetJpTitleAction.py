def GetJpTitleAction(soup):
    jp_title_field = soup.find('div', class_="subject")
    if jp_title_field:
        return jp_title_field.text
from atm_cli_tools.Server.UseCase.Spreadsheet.CheckWebmUrlAction import CheckWebmUrlAction
import time

def CheckWebmUrlsAction(themes: list)-> list:
    undownload_themes = []
    for theme in themes:
        if CheckWebmUrlAction(theme['webm_url']) == False:
            undownload_themes.append(theme)
        time.sleep(0.2)
    return undownload_themes
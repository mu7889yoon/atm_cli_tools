import sys
from theme import Props

args = sys.argv
url = args[1]
props = Props(url)
print(props.theme_url)
print(props.slug_anime_name)
print(props.webm_url)

props.renamer()
print(props.en_theme_name)

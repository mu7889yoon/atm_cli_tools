# atm_cli_tools
Download and translate the file name to Japanese

[日本語版README](/README_jp.md)
## Features
- Download the theme file
- Translate the file name to Japanese Anime Title & Theme Name

## Usage
```
atdl [-h] [-f] url

positional arguments:
  url         URL of the theme page

options:
  -h, --help  show this help message and exit
  -f, --fast  Without rename, Just Download
```

## Installation
```
pip install pyinstaller
pyinstaller -F atm_tools.py -n atdl
```
move ```./atdl``` to environment variable path.
Then you can use ```atdl``` command.

## Attention 
Sometimes it does not work translate well.
__Pull requests are welcome.__


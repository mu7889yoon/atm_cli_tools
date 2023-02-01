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
### Build yourself

```
git clone 'https://github.com/mu7889yoon/atm_cli_tools'
cd atm_cli_tools
pip install pyinstaller
pyinstaller -F atm_tools.py -n atdl
```
move ```./atdl``` to environment variable path.
Then you can use ```atdl``` command.

### Download
[![MacOS](https://img.shields.io/badge/-MacOS-lightblue.svg?style=for-the-badge&logo=apple)](https://github.com/mu7889yoon/atm_cli_tools/releases/latest/download/atdl.dmg) [![Windows](https://img.shields.io/badge/-Windows_x64-blue.svg?style=for-the-badge&logo=windows)](https://github.com/mu7889yoon/atm_cli_tools/releases/latest/download/atdl.exe)

Move the downloaded file to the directory where the environment variable path is set.
Then you can use ```atdl``` command.
## Attention 
Sometimes it does not work translate well.
__Pull requests are welcome.__


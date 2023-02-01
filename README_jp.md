# atm_cli_tools
ダウンロードとファイル名の日本語化を行います

## 機能
- OPEDのダウンロード
- ファイル名を日本語のアニメタイトルと曲名に翻訳

## 使い方
```
atdl [-h] [-f] url
```
```
  url         URL of the theme page
```
ダウンロード対象のURLを指定してください

```
  -h, --help  show this help message and exit
  -f, --fast  Without rename, Just Download
```
```-h```,```--help```オプションを指定すると、ヘルプを表示します。現在は、```-f```,```--fast```オプションのみですが、後々追加されるかもしれません。

```-f```,```--fast```オプションを指定すると、ファイル名の日本語化なしでダウンロードします。
急いでいるときに使ってください(サビが始まっても次の曲がわからない時など)

## インストール
### 自分でビルドする場合
```
git clone 'https://github.com/mu7889yoon/atm_cli_tools'
cd atm_cli_tools
pip install pyinstaller
pyinstaller -F atm_tools.py -n atdl
```
```./atdl```をパスが通っているディレクトリに移動してください。

```atdl```コマンドが使えるようになります。

### ダウンロードする場合
[![MacOS](https://img.shields.io/badge/-MacOS-lightblue.svg?style=for-the-badge&logo=apple)](https://github.com/mu7889yoon/atm_cli_tools/releases/latest/download/atdl.dmg) [![Windows](https://img.shields.io/badge/-Windows_x64-blue.svg?style=for-the-badge&logo=windows)](https://github.com/mu7889yoon/atm_cli_tools/releases/latest/download/atdl.exe)

ダウンロードしたファイルをパスが通っているディレクトリに移動することで、```atdl```コマンドが使えるようになります。

## 注意
翻訳がうまくいかないことがあります、許して

__プルリクエスト大歓迎です__
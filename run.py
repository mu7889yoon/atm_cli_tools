# from atm_cli_tools.Server.Controller.BatchController import BatchControllerClass
import os
from dotenv import load_dotenv
from fuga import *

# .envファイルの内容を読み込見込む
load_dotenv()

# os.environを用いて環境変数を表示させます
print(os.environ['GAS_WEBM_LOGS_API'])
printval()

year = 2024
season = 'winter'



# BatchControllerClass(year, season).fetch_params()
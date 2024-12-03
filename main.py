# 必要なライブラリをインポート
import requests
import flet as ft
import json
from datetime import datetime

# 定数を定義
DATA_FILE = "jma/weather_info.json"
WEATHER_API_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/{office_code}.json"

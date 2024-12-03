# 必要なライブラリをインポート
import requests
import flet as ft
import json
from datetime import datetime

# 定数を定義
DATA_FILE = "jma/weather_info.json"
WEATHER_API_URL = "https://www.jma.go.jp/bosai/forecast/data/forecast/{office_code}.json"

# 日付フォーマット関数
def format_date(date_str: str) -> str:
    date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return date.strftime("%Y年%m月%d日")

# 天気アイコンを取得する関数
def get_weather_icon(weather_code: str) -> str:
    weather_icons = {
        "100": "☀️",  # 晴れ
        "101": "🌤️",  # 晴れ時々曇り
        "102": "🌦️",  # 晴れ時々雨
        "200": "☁️",  # 曇り
        "300": "🌧️",  # 雨
        "317": "🌧️❄️☁️",  # 雨か雪のち曇り
        "400": "❄️",  # 雪
        "402": "❄️☁️",  # 雪時々曇り
        "500": "⛈️",  # 雷雨
        "413": "❄️→🌧️",  # 雪のち雨
        "314": "🌧️→❄️",  # 雨のち雪
        "201": "🌤️",
        "202": "☁️🌧️",
        "218": "☁️❄️",
        "270": "❄️☁️",
        "206": "🌧️☁️",
        "111": "🌧️☀️",
        "112": "🌧️❄️",
        "211": "❄️☀️",
        "212": "❄️☁️",
        "313": "❄️🌧️",
        "203": "☁️❄️",
        "302": "❄️",
        "114": "❄️☀️",
        "214":"☁️🌧️",
        "204":"☁️❄️⚡️",
        "207":"☁️🌧️❄️",
        "110":"☀️☁️",
    }
    # 該当する天気コードがない場合は ❓ を表示
    return weather_icons.get(weather_code, "❓")
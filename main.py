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

def get_weather_text(code: str) -> str:
    # 天気コードに対応する天気を返す
    weather_codes = {
        "100": "晴れ",
        "101": "晴れ時々曇り",
        "102": "晴れ時々雨",
        "200": "曇り",
        "201": "曇り時々晴れ",
        "202": "曇り時々雨",
        "218": "曇り時々雪",
        "270": "雪時々曇り",
        "300": "雨",
        "317": "雨か雪のち曇り",
        "400": "雪",
        "402": "雪時々曇り",
        "500": "雷雨",
        "413": "雪のち雨",
        "206": "雨時々曇り",
        "111": "雨時々晴れ",
        "112": "雨時々雪",
        "211": "雪時々晴れ",
        "206": "雨時々曇り",
        "212": "雪時々曇り",
        "313": "雪のち雨",
        "314": "雨のち雪",
        "203": "曇り時々雪",
        "302": "雪",
        "114": "雪時々晴れ",
        "214":"曇り後雨",
        "204":"曇り時々雪で雷を伴う",
        "207":"曇り時々雨か雪",
        "110":"晴れのち時々曇り",
    }
    return weather_codes.get(code, f"不明な天気 (コード: {code})")

def main(page: ft.Page):
    page.title = "天気予報アプリ"
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.colors.LIGHT_BLUE_50

    # ヘッダーにタイトル
    header = ft.Container(
        content=ft.Text("日本の天気予報", size=30, weight="bold", color=ft.colors.WHITE),
        padding=20,
        bgcolor=ft.colors.CYAN_800,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(5),
    )

    # JSONデータを読み込む
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        page.add(ft.Text("JSONファイルが見つかりません。", color=ft.colors.RED))
        return
    except json.JSONDecodeError as e:
        page.add(ft.Text(f"JSONデータの読み込みに失敗しました: {e}", color=ft.colors.RED))
        return

    centers = data.get("centers", {})
    offices = data.get("offices", {})
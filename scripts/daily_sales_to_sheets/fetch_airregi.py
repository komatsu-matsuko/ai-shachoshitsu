# エアレジ データ連携API で 店内売上・客数 を取得
# 公式ドキュメント: https://faq.airregi.jp/hc/ja/articles/48202752451353

import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def fetch_airregi_daily(date: datetime) -> dict:
    """
    指定日のエアレジデータを取得する。
    戻り値は「日次売上報告」の列に合わせたキーで揃える。
    実際のエアレジAPIのエンドポイント・パラメータは公式ドキュメントで確認し、ここを実装する。
    """
    api_key = os.getenv("AIRREGI_API_KEY")
    api_token = os.getenv("AIRREGI_API_TOKEN")
    if not api_key or not api_token:
        return {"error": "AIRREGI_API_KEY / AIRREGI_API_TOKEN が未設定です"}

    # TODO: エアレジ データ連携API の実際のエンドポイントに置き換える
    # 例: 取引一覧や日次集計を返す API を叩き、時間帯別に集計
    # url = "https://api.airregi.jp/..."  # 公式ドキュメントで確認
    # headers = {"Authorization": f"Bearer {api_token}", "X-API-Key": api_key}
    # params = {"date": date.strftime("%Y-%m-%d")}
    # res = requests.get(url, headers=headers, params=params)

    # 仮の戻り値（実装時に API レスポンスから埋める）
    return {
        "date": date.strftime("%Y/%m/%d"),
        "in_store_11_15_guests": 0,
        "in_store_11_15_sales": 0,
        "in_store_17_23_guests": 0,
        "in_store_17_23_sales": 0,
        "in_store_23_29_guests": 0,
        "in_store_23_29_sales": 0,
        "in_store_avg_unit_price": 0,
        "total_guests": 0,
        "total_sales": 0,
    }

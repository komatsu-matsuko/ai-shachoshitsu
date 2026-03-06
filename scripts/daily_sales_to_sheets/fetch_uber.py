# Uber Eats Reporting API で Uber 売上・件数を取得
# https://developer.uber.com/docs/eats/guides/reporting

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def fetch_uber_daily(date: datetime) -> dict:
    """
    指定日の Uber Eats データを取得する。
    OAuth トークン取得が必要な場合は別スクリプトでトークンを取得し、ここでは UBER_ACCESS_TOKEN を使用する想定。
    """
    token = os.getenv("UBER_ACCESS_TOKEN")
    if not token:
        return {"error": "UBER_ACCESS_TOKEN が未設定です（または OAuth でトークン取得が必要）"}

    # TODO: Uber Eats Reporting API のエンドポイントに置き換える
    # 例: POST /v1/eats-report 等。公式ドキュメントで確認
    # url = "https://api.uber.com/v1/eats/report"
    # headers = {"Authorization": f"Bearer {token}"}
    # res = requests.post(url, headers=headers, json={...})

    return {
        "date": date.strftime("%Y/%m/%d"),
        "uber_11_15_guests": 0,
        "uber_11_15_sales": 0,
        "uber_17_23_guests": 0,
        "uber_17_23_sales": 0,
        "uber_23_29_guests": 0,
        "uber_23_29_sales": 0,
        "uber_avg_unit_price": 0,
        "uber_total_guests": 0,
        "uber_total_sales": 0,
    }

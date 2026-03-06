# LINE Messaging API の統計で友だち数（登録者数）を取得
# GET https://api.line.me/v2/bot/insight/followers?date=YYYYMMDD

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def fetch_line_followers(date: datetime) -> dict:
    """
    指定日時点の LINE 友だち数（登録者数）を取得する。
    """
    token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    if not token:
        return {"error": "LINE_CHANNEL_ACCESS_TOKEN が未設定です", "followers": 0}

    url = "https://api.line.me/v2/bot/insight/followers"
    params = {"date": date.strftime("%Y%m%d")}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        data = res.json()
        return {
            "date": date.strftime("%Y/%m/%d"),
            "followers": data.get("followers", 0),
            "targeted_reaches": data.get("targetedReaches", 0),
            "blocks": data.get("blocks", 0),
        }
    except Exception as e:
        return {"error": str(e), "followers": 0}

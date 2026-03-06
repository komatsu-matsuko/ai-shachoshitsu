#!/usr/bin/env python3
"""
日次売上 自動投入スクリプト

エアレジ・Uber・LINE からデータを取得し、Google スプレッドシート「日次売上報告」に 1 行追記する。
実行: 毎日 1 回（タスクスケジューラ / cron / Cowork 等）

使い方:
  pip install -r requirements.txt
  cp .env.example .env  →  .env に認証情報を記入
  python main.py
"""

import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

# 前日分を記録する想定（実行時刻が翌朝なら「昨日」）
TARGET_DATE = datetime.now() - timedelta(days=1)


def main():
    print(f"[日次売上] 対象日: {TARGET_DATE.strftime('%Y-%m-%d')}")

    # 1. エアレジ
    try:
        from fetch_airregi import fetch_airregi_daily
        airregi = fetch_airregi_daily(TARGET_DATE)
        if "error" in airregi:
            print(f"  エアレジ: {airregi['error']}")
            airregi = {}
    except Exception as e:
        print(f"  エアレジ 取得失敗: {e}")
        airregi = {}

    # 2. Uber
    try:
        from fetch_uber import fetch_uber_daily
        uber = fetch_uber_daily(TARGET_DATE)
        if "error" in uber:
            print(f"  Uber: {uber['error']}")
            uber = {}
    except Exception as e:
        print(f"  Uber 取得失敗: {e}")
        uber = {}

    # 3. LINE
    try:
        from fetch_line import fetch_line_followers
        line = fetch_line_followers(TARGET_DATE)
        if "error" in line:
            print(f"  LINE: {line['error']}")
        line_followers = line.get("followers", 0)
    except Exception as e:
        print(f"  LINE 取得失敗: {e}")
        line_followers = 0

    # 4. 1 行分のリストにまとめる（スプレッドシートの列順に合わせる）
    row = build_row(TARGET_DATE, airregi, uber, line_followers)

    # 5. Google Sheets に追記
    try:
        from write_sheets import get_sheets_service, append_daily_row
        service = get_sheets_service()
        append_daily_row(service, row)
        print("  Google Sheets に追記しました。")
    except FileNotFoundError as e:
        print(f"  {e}")
        sys.exit(1)
    except Exception as e:
        print(f"  Sheets 書き込み失敗: {e}")
        sys.exit(1)

    print("[日次売上] 完了")


def build_row(date: datetime, airregi: dict, uber: dict, line_followers: int) -> list:
    """
    「日次売上報告」の 1 行をリストで返す。
    列順は実際のスプレッドシートに合わせて調整すること。
    """
    # 仮の列順（実際のシートに合わせて並べ替え）
    return [
        date.strftime("%Y/%m/%d"),
        "",  # 担当者
        airregi.get("in_store_11_15_guests", ""),
        airregi.get("in_store_11_15_sales", ""),
        uber.get("uber_11_15_guests", ""),
        uber.get("uber_11_15_sales", ""),
        airregi.get("in_store_17_23_guests", ""),
        airregi.get("in_store_17_23_sales", ""),
        uber.get("uber_17_23_guests", ""),
        uber.get("uber_17_23_sales", ""),
        airregi.get("in_store_23_29_guests", ""),
        airregi.get("in_store_23_29_sales", ""),
        uber.get("uber_23_29_guests", ""),
        uber.get("uber_23_29_sales", ""),
        "",  # チラシ配布数
        line_followers,  # LINE増加数（当日の友だち数 or 前日比は別ロジックで）
        airregi.get("in_store_avg_unit_price", ""),
        uber.get("uber_avg_unit_price", ""),
        airregi.get("total_guests", ""),
        airregi.get("total_sales", ""),
        uber.get("uber_total_guests", ""),
        uber.get("uber_total_sales", ""),
        "",  # 店内外装客数（計算で出す場合はここで）
        "",  # 店内外総売上
        "",  # 特記事項
    ]


if __name__ == "__main__":
    main()

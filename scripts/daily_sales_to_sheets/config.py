# 設定：スプレッドシートID・シート名・書き込み範囲
# 環境変数から読み、なければここでデフォルトを指定

import os
from dotenv import load_dotenv

load_dotenv()

# Google スプレッドシート
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "16nmlFxS85gxzGIFqcxKzHW4845plF3yKuS3WX8vkRrk")
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "日次売上報告")

# 書き込む行：今日の日付の行を特定するか、次の空き行に追記する
# 列は「日次売上報告」のレイアウトに合わせて write_sheets.py で指定

# エアレジ
AIRREGI_API_KEY = os.getenv("AIRREGI_API_KEY", "")
AIRREGI_API_TOKEN = os.getenv("AIRREGI_API_TOKEN", "")

# Uber Eats
UBER_CLIENT_ID = os.getenv("UBER_CLIENT_ID", "")
UBER_CLIENT_SECRET = os.getenv("UBER_CLIENT_SECRET", "")
UBER_ACCESS_TOKEN = os.getenv("UBER_ACCESS_TOKEN", "")

# LINE
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")

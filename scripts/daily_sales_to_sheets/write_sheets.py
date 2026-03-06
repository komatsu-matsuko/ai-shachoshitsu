# Google Sheets API で「日次売上報告」に 1 行追記

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import config

# 書き込む列は「日次売上報告」の実際の列順に合わせて調整する
def get_sheets_service():
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        raise FileNotFoundError("GOOGLE_APPLICATION_CREDENTIALS の JSON キーファイルが見つかりません")
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=scopes)
    return build("sheets", "v4", credentials=creds)


def append_daily_row(service, row_values: list):
    """
    日次売上報告シートに 1 行追加する。
    row_values は [日付, 担当者, 店内11-15客数, 店内11-15売上, ...] の順でリストにする。
    """
    sheet_id = config.GOOGLE_SHEET_ID
    range_name = f"'{config.GOOGLE_SHEET_NAME}'!A:Z"  # 次の空き行に追記する場合は append を使う
    body = {"values": [row_values]}
    try:
        result = (
            service.spreadsheets()
            .values()
            .append(
                spreadsheetId=sheet_id,
                range=range_name,
                valueInputOption="USER_ENTERED",
                insertDataOption="INSERT_ROWS",
                body=body,
            )
            .execute()
        )
        return result
    except HttpError as e:
        raise RuntimeError(f"Google Sheets 書き込みエラー: {e}") from e

# 日次売上 自動投入スクリプト

Uber・エアレジ・LINE の数字を **手入力せず**、API で取得して Google スプレッドシート「日次売上報告」に自動で 1 行追記するためのスクリプトです。

## 前提

- **エアレジ**：データ連携API の API キー・トークンを発行済みであること
- **Uber Eats**：Reporting API 利用可能（要申請・OAuth の場合はトークン取得）
- **LINE**：Messaging API のチャネルがあり、Channel Access Token があること
- **Google**：サービスアカウントの JSON キーを取得し、対象スプレッドシートをそのアカウントと「編集可」で共有済みであること

## セットアップ（社員 PC で実行する場合）

1. **Python 3.8 以上** をインストールする。

2. このフォルダで:
   ```bash
   cd scripts/daily_sales_to_sheets
   pip install -r requirements.txt
   cp .env.example .env
   ```

3. **.env** を開き、Notion 等で管理している認証情報を記入する。
   - エアレジ: `AIRREGI_API_KEY`, `AIRREGI_API_TOKEN`
   - Uber: `UBER_ACCESS_TOKEN` または OAuth 用の `UBER_CLIENT_ID` / `UBER_CLIENT_SECRET`
   - LINE: `LINE_CHANNEL_ACCESS_TOKEN`
   - Google: `GOOGLE_APPLICATION_CREDENTIALS` にサービスアカウント JSON のパス、`GOOGLE_SHEET_ID` はそのままでも可

4. **Google サービスアカウント** の JSON をこのフォルダの `credentials/` などに置き、`.env` の `GOOGLE_APPLICATION_CREDENTIALS` にそのパスを書く。

5. エアレジ・Uber の **実際の API エンドポイント** が分かったら、`fetch_airregi.py` と `fetch_uber.py` の `# TODO` を実装する。LINE は `fetch_line.py` でそのまま利用可能。

## 実行

```bash
python main.py
```

- デフォルトでは「前日」のデータを取得し、スプレッドシートに 1 行追記する。

## 毎日自動実行（Cowork や社員 PC）

- **Windows**：タスクスケジューラで「毎日 朝 6:00」などに `python C:\...\main.py` を実行するように設定。
- **Mac**：cron で `0 6 * * * cd /path/to/scripts/daily_sales_to_sheets && python main.py` を登録。
- **Cowork**：上記コマンドを「日次ジョブ」として 1 回実行するように組み込む。

## 仕様の詳細

- 実装仕様・データマッピング・段階的導入は **company-memory/06_operations/日次売上_自動化_実装仕様.md** を参照。

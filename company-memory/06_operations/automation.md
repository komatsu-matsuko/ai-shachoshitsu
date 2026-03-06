# 自動化状況

## 日次売上レポート（完全自動化）

- **現状**：スタッフが毎日 Uber・エアレジ・LINE にブラウザでログインし、手入力で Google スプレッドシートに入力している。
- **目標**：手入力ゼロ。API で 3 ソースを取得し、スプレッドシートに自動追記。
- **実装**：
  - 仕様：`06_operations/日次売上_自動化_実装仕様.md`
  - スクリプト：プロジェクト直下 `scripts/daily_sales_to_sheets/`（Python）
  - 実行：社員 PC のタスクスケジューラ / cron、または Cowork で毎日 1 回実行。
- **データソース**：エアレジ API、Uber Eats Reporting API、LINE Messaging API（統計）、Google Sheets API。
- **認証**：すべて .env で管理。Notion 等に保管し、スクリプトには渡すだけ。

## その他

- 導入済み・検討中の自動化があれば追記。

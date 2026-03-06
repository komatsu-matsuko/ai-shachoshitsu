# アクティブプロジェクト

## 日次売上の完全自動化（Uber・エアレジ・LINE → Google Sheets）

- **目的**：手入力ゼロで「日次売上報告」スプレッドシートを毎日自動更新する
- **主担当**：相沢
- **実装担当**：工藤
- **期限**：2026-03-07（明日中に実行設計まで）
- **参照**：`company-memory/06_operations/日次売上_自動化_実装仕様.md` / `scripts/README_automation.md` / `company-memory/10_dashboard/明日やること.md`

### 明日の成果物（Definition of Done）

- 認証情報（エアレジ / Google / LINE / Uber）の取得手順が確定し、保管先（Notion）と受け渡し方法（.env）が明文化されている
- `scripts/daily_sales_to_sheets/main.py` が実行できる状態（少なくとも Sheets 書き込みと LINE 取得は動作確認済み）
- エアレジ・Uber は「取得方式（API）と不足情報（エンドポイント/権限/申請）」が洗い出され、次アクションがタスク化されている

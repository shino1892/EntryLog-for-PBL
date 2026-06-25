# EntryLog - Felica Attendance System

Felica カード（学生証など）を使用して出席管理を行う Python ベースのシステムです。
Raspberry Pi zero 2w 等のデバイスに PaSoRi（Felica リーダー）を接続して動作させることを想定しています。
記録されたデータは MySQL データベースに保存されます。

## 機能

- **出席記録**: Felica カードをタッチするだけで出席時刻を記録。
- **ユーザー登録**: 新しいカードをスキャンし、学生番号と紐付けて登録。
- **サーバー連携**: 出席ログやカード登録情報を外部サーバーへ送信（API 連携）。
- **DB**: MySQL を使用した堅牢なデータ管理。
- **音声フィードバック**: 操作成功時やエラー時にブザー音で通知。

### ハードウェア

- Raspberry Pi zero 2w(または互換性のある Linux デバイス)
- Sony PaSoRi (RC-S380) - Felica リーダー
- Grove Base Hat & Grove Buzzer (オプション: 音声通知用)

### ソフトウェア

- Python 3.12.3
- `libpafe` (Felica 制御用 C ライブラリ)

## インストール

1.  **リポジトリのクローン**

    ```bash
    git clone <repository-url>
    cd entry_log_for_PBL
    ```

2.  **依存ライブラリのインストール**

    ```bash
    pip install -r requirements.txt
    ```

3.  **libpafe のセットアップ**
    環境に合わせて `libpafe` をインストールし、ライブラリファイル（`.so` や `.dll`）へのパスを確認してください。

## 設定

プロジェクトルートの `.env.example` ファイルをコピーし、`.env`として保存して以下の環境変数を必ず設定してください。

```ini
DB_HOST = 
DB_USER = 
DB_PASS = 
DB_PORT = 
DB_NAME = 

LIBPAFE_PATH=/usr/local/lib/libpafe.so
```

- `DB_HOST`: データベースのIPアドレス。
- `DB_USER`: データベースのユーザー名。
- `DB_PASS`: データベースのパスワード。
- `DB_PORT`: データベースのポート番号。
- `DB_NAME`: データベースの名前。
- `LIBPAFE_PATH`: インストールした `libpafe` ライブラリへのパス。

## 使い方

### メインプログラムの実行

```bash
python main.py
```

起動すると、以下のメニューが表示されます。

1.  **Student Registration Mode**: 学生証（Felica カード）と学生番号を紐付けて登録します。
2.  **Attendance Recording Mode**: 出席記録モードを開始します。カードをかざすと出席時刻が記録されます。
3.  **Exit**: プログラムを終了します。

運用時は、まず `1` を選択してユーザー登録を行い、その後 `2` を選択して出席記録の待機状態にします。

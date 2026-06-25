import mysql.connector
import app.config as cfg

def db_connect():
    try:
        return mysql.connector.connect(
                host=cfg.DB_HOST,
                port=cfg.DB_PORT,
                user=cfg.DB_USER,
                password=cfg.DB_PASS,
                database=cfg.DB_NAME
                )
    
    except Exception as e:
        print(f"データベース接続エラー: {e}")
        return

# DB接続テスト
if __name__ == "__main__":
    conn = db_connect()
    print(conn)
import mysql

import mysql.connector

def add_entry(conn, student_num: int, timestamp):
    try:
        sql = "INSERT INTO entry (user_id, timestamp) VALUES (%s, %s)"
        with conn.cursor() as cursor:
            cursor.execute(sql, (student_num, timestamp))
            
            if cursor.rowcount > 0:
                conn.commit()  # 正常時のみコミット
                return True
            else:
                conn.rollback()  # 影響行数0ならロールバック
                raise RuntimeError("Failed to Entry.")
                
    except mysql.connector.IntegrityError as e:
        conn.rollback()  # ★制約違反時も確実にロールバックしてロック解放
        print(f"Integrity Error (add_entry): {e}")  # ログを出しておくとデバッグが楽になります
        return False
        
    except Exception as e:
        conn.rollback()  # ★その他のエラー時も確実にロールバック
        print(f"Database Error (add_entry): {e}")
        return None
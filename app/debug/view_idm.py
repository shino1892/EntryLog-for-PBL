import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utility.db_connect import db_connect

def view_users():
    conn = db_connect()
    res = None
    try:
        sql = "SELECT id, idm, user_id FROM idms"
        with conn.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
    except Exception as e:
        print(f"Database Error (view_users): {e}")
        return None
    finally:
        conn.close()

    # 取得したデータの表示
    if not res:
        print("登録されているユーザーはありません。")
    else:
        print("\n登録ユーザー一覧:")
        print("-" * 42)
        print(f"{'ID':<6} {'IDm':<20} {'学籍番号':<10}")
        print("-" * 42)
        
        # データベースから取得した各行（user）を表示
        for user in res:
            # user[0] = id
            # user[1] = idm
            # user[2] = user_id
            print(f"{user[0]:<6} {user[1]:<20} {user[2]:<10}")
            
        print("-" * 42)

if __name__ == "__main__":
    view_users()
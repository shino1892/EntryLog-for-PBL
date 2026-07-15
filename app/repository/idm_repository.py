def get_user_by_idm(conn, idm: str):
    try:
        sql = "SELECT id, idm, user_id FROM idms WHERE idm = %s"
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (idm,))
            res = cursor.fetchone()
            return res
    except Exception as e:
        print(f"Database Error (get_user_by_idm): {e}")
        return None

# 2. 修正：引数の説明を user_id に統一
def regist_user(conn, idm: str, user_id: int):
    try:
        sql = "INSERT INTO idms (idm, user_id) VALUES (%s, %s)"
        with conn.cursor() as cursor:
            cursor.execute(sql, (idm, user_id))
            conn.commit()
            if cursor.rowcount > 0:
                return cursor.lastrowid
            else:
                raise RuntimeError("User registration failed.")
    except Exception as e:
        # 前回の質問の通り、user_id が student_users に存在しない場合は
        # ここで外部キー制約エラー（Cannot add or update a child row...）がキャッチされます
        print(f"Database Error (regist_user): {e}")
        return None
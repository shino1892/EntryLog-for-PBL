def get_user_by_idm(conn, idm:str):
    try:
        sql = "SELECT id, idm, student_num FROM users WHERE = %s"
        with conn.cursor(dictionary = True) as cursor:
            cursor.execute(sql,(idm,))
            res = cursor.fetchone()
            return res
    except Exception as e:
        print(f"Database Error (get_user_by_idm): {e}")
        return None

def regist_user(conn, idm:str, student_num:int):
    try:
        sql = "INSERT INTO users (idm, student_num) VALUES (%s, %s)"
        with conn.cursor() as cursor:
            cursor.execute(sql,(idm, student_num,))
            conn.commit()
            if cursor.rowcount > 0:
                return cursor.lastrowid
            else:
                raise RuntimeError("User registration failed.")
    except Exception as e:
        print(f"Database Error (regist_user): {e}")
        return None
import mysql

def add_entry(conn, student_num:int, timestamp):
    try:
        sql = "INSERT INTO entry (user_id,timestamp) VALUES (%s,%s)"
        with conn.cursor() as cursor:
            cursor.execute(sql,(student_num, timestamp,))
            conn.commit()
            if cursor.rowcount > 0:
                return True
            else:
                raise RuntimeError("Failed to Entry.")
    except mysql.connector.IntegrityError:
        return False
    except Exception as e:
        print(f"Database Error (add_entry): {e}")
        return None
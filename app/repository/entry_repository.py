import mysql

def add_entry(conn, idm:str, timestamp):
    try:
        sql = "INSERT INTO entry (num,timestamp) VALUES (%s,%s)"
        with conn.cursor() as cursor:
            cursor.execute(sql,(idm,timestamp,))
            conn.commit()
            if conn.rowcount > 0:
                return True
            else:
                raise RuntimeError("Failed to Entry.")
    except mysql.connector.IntegrityError:
        return False
    except Exception as e:
        print(f"Database Error (add_entry): {e}")
        return None
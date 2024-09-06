# Update: 데이터 수정 함수
def update_data(user_id, new_age):
    conn = connect_db() # type: ignore
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        sql = "UPDATE users SET age = %s WHERE id = %s"
        val = (new_age, user_id)
        cursor.execute(sql, val)
        conn.commit()
        print(f"{cursor.rowcount} record(s) updated.")
    except mysql.connector.Error as e: # type: ignore
        print(f"Error during data update: {e}")
    finally:
        cursor.close()
        conn.close()

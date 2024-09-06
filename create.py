import mysql.connector

def create_customer(name, gender, email, birthYear):
    conn = mysql.connector.connect(
        host='192.168.0.92',
        user='test',
        password='88Einstein$',
        database='pub'
    )
    cursor = conn.cursor()

    sql = "INSERT INTO customers (name, gender, email, birthYear) VALUES (%s, %s, %s, %d)"
    values = (name, gender, email, birthYear)
    
    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Customer added successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Example usage
create_customer('John', 'man', 'john.doe@example.com', '2024')


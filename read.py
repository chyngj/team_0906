import mysql.connector
from mysql.connector import Error

# 데이터베이스 연결하는 함수
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        if connection.is_connected():
            print(f"Connected to MySQL database '{db_name}' at {host_name}")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

# 데이터베이스에서 customer 테이블의 데이터를 읽는 함수
def read_all_customers(conn):
    query = "SELECT * FROM customer"  # 'customer' 테이블의 모든 데이터를 가져오는 쿼리
    return read_data(conn, query)

# 데이터베이스에서 데이터를 읽는 함수
def read_data(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()  # 모든 결과를 리스트로 가져옴
        return result
    except Error as e:
        print(f"Error reading data: {e}")
        return []

# 데이터베이스 사용
if __name__ == "__main__":
    mysql_host = "192.168.0.92"  # MySQL 서버 IP
    mysql_user = "test"          # MySQL 사용자 이름
    mysql_password = "88Einstein$"  # MySQL 비밀번호
    mysql_database = "team0906"  # 사용할 데이터베이스 이름

    # 데이터베이스 연결
    connection = create_connection(mysql_host, mysql_user, mysql_password, mysql_database)
    
    if connection:
        # 고객 데이터 읽기
        customers = read_all_customers(connection)
        print("Customers:")
        for customer in customers:
            print(customer)
        
        # 연결 종료
        connection.close()

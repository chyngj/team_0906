import mysql.connector
from config import read_config

def read_customers():
    # 설정 파일에서 데이터베이스 설정 읽기
    config = read_config()

    # 고객 데이터를 가져오는 SQL 쿼리
    query = "SELECT * FROM customers"

    try:
        # 데이터베이스 연결 설정
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # 쿼리 실행
        cursor.execute(query)

        # 쿼리 결과에서 모든 행 가져오기
        result = cursor.fetchall()

        # 결과가 있는지 확인
        if result:
            # 각 고객 레코드 출력
            for row in result:
                print(row)
        else:
            print("고객 데이터를 찾을 수 없습니다.")

    except mysql.connector.Error as e:
        print(f"오류: {e}")
    
    finally:
        cursor.close()
        conn.close()

# 사용 예시
if __name__ == '__main__':
    read_customers()


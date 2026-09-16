# 문1) 부서명을 입력(로그인)하여 성공하면 아래의 내용 출력
# 직원번호 입력 : _______
# 직원명 입력 : _______
# 직원번호 직원명 부서번호 부서전화 직급 성별
# 1         홍길동 10   111-1111 이사 남 
# ...
#   
import MySQLdb
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'host':os.getenv('DB_HOST'),
    'user':os.getenv('DB_USER'),
    'password':os.getenv('DB_PASSWORD'),
    'database':os.getenv('DB_NAME'),
    'port':int(os.getenv('DB_PORT')),  # port는 숫자 처리
    'charset':os.getenv('DB_CHARSET')
}

def LoginFunc():
    conn = None

    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        jikwon_no = input("직원번호 입력 : ")
        jikwon_name = input("직원명 입력 : ")

        if jikwon_no == "" or jikwon_name == "":
            print("로그인 정보를 입력하세요.")
            return

        sql = """
            SELECT j.jikwonno as 직원번호,j.jikwonname as 직원명,
            b.busername as 부서명,b.busertel as 부서번호,
            j.jikwonjik as 직급,j.jikwongen as 성별
            FROM jikwon AS j
            LEFT JOIN buser AS b ON j.busernum = b.buserno
            WHERE j.jikwonno = %s AND j.jikwonname = %s
        """

        cursor.execute(sql, (jikwon_no, jikwon_name))
        data = cursor.fetchone()

        if data:
            print("\n로그인 성공")
            print("직원번호 직원명 부서명 부서전화 직급 성별")
            print(data[0], data[1], data[2],data[3], data[4], data[5])
        else:
            print("로그인 실패: 입력자료 확인하세요.")

    except Exception as e:
        print("에러:", e)

    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    LoginFunc()

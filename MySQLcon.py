import pymysql as psql

try:
    con = psql.connect(
        host="localhost",
        user="root",
        password="123",
        database="example",
        charset="utf8"
    )
    cur = con.cursor()
    #MySQL 테이블 생성
    #cur.execute("CREATE TABLE users(name TEXT, email TEXT)")

    #데이터 추가
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cur.execute(sql, ("김철수", "kim@test.com"))
    cur.execute(sql, ("이천수", "lee@test.com"))
    con.commit()

    #확인
    sql = "SELECT * FROM users"
    cur.execute(sql)
    print(cur.fetchall())
          
    #수정
    sql = "UPDATE users SET name=%s WHERE email =%s"
    cur.execute(sql,("김길동","kim@test.com"))
    con.commit()

    #확인
    sql = "SELECT * FROM users"
    cur.execute(sql)
    print(cur.fetchall())

    #제거
    sql = "DELETE FROM users WHERE email =%s"
    cur.execute(sql, ("lee@test.com",))
    con.commit()

    #전부 제거
    #sql = "DELETE FROM users"
    #cur.execute(sql)
    #con.commit()

except Exception as e:
    print("에러 발생:", e)
    con.rollback()  # 문제가 생기면 변경 내용을 취소

finally:

    #테이블 확인
    sql = "SELECT * FROM users"
    cur.execute(sql)
    print(cur.fetchall())

    # 자원 정리
    cur.close()
    con.close()
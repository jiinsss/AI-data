import pymysql
import base64
from io import BytesIO

def create_connection():
    connect = pymysql.connect(host='host.docker.internal', 
                          port=3307, 
                          user='root', 
                          password='', 
                          db='mysql-db', 
                          charset='utf8')

    cur = connect.cursor()

    return connect, cur

#img,name 업로드
def insert_data1(option1,binary_image):
    conn,cursor=create_connection()
    binary_image=binary_image
    try:
        query = f'INSERT INTO imgtable (게임이름,이미지_파일) VALUES("{option1}",%s)'
        cursor.execute(query,binary_image)
        conn.commit()
        #print('success')
    except:
        #print('fail')
        pass

#시간','유저네임','리뷰','점수','추천수
def insert_data2(option1,option2,option3,option4,option5):
    conn,cursor=create_connection()
    try:
        query = f'INSERT INTO reviewtable (시간,유저네임,리뷰,점수,추천수) VALUES("{option1}","{option2}","{option3}","{option4}","{option5}")'
        cursor.execute(query)
        conn.commit()
    except:
        pass



#39dbSelect.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")

    db = client['test'] # 데이터베이스 접근

    print('저자', '제목', '종류')
    print('='*50)
    for d in db["posts"].find(): # find() == SELECT * FROM 테이블명
        print(d['author'], d['title'], d['kind'])

    print('-'*50)
    print('전체 레코드 갯수 : ', db['posts'].estimated_document_count())
    print() # 공백
    name = input('저자검색입력 >>>') # SELECT * FROM table WHERE author = '...';
    #search = client.test.posts.find({'author' : name})
    search = db['posts'].find_one({'author' : name})
    #print(search)

    if search is None :
        print(name, ' 검색 결과가 없습니다.')
        exit(-1) # 아래 문장은 더이상 수행하지 않음

    print(search['author'], search['title'], search['kind'])

    print('------------- 저자 like조건으로 검색하기 -------------')
    time.sleep(2)

    name2 = input('저자검색입력 like >>>') # SELECT * FROM table WHERE author like '%...%';
    search2 = db['posts'].find({'author' : {'$regex': name2}}) # /^~$ 없이 정규식을 쓰면 포함되어있는 것도 다 true로 처리하니까~
    for d2 in search2 :
        print(d2['author'], d2['title'], d2['kind'])

except Exception as err:
    print('db조회에러발생 : ', err)
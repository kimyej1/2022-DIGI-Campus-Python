#40dbDelete.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['test']

    # delete_one() 사용해서 삭제 처리 후 전체 출력
    name = input('삭제 데이터 저자 입력 >>>')
    search = db['posts'].find_one({'author': name})

    if search is None:
        print('삭제할 데이터가 없습니다.')
        exit(-1)

    db['posts'].delete_one({'author' : name})
    print('삭제가 완료되었습니다. [삭제 후 데이터 목록...]')

    for d in db['posts'].find():
        print(d)

except Exception as err:
    print('db조회에러발생 : ', err)
#41dbUpdate.py
from pymongo import MongoClient
import time

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client['test']

    name = input('수정 데이터 저자 입력 >>>')
    search = db['posts'].find_one({'author': name})

    if search is None:
        print('수정할 데이터가 없습니다.')
        exit(-1)

    data_author = input('이름수정입력 >>>')
    data_title = input('제목수정입력 >>>')
    data_kind = input('종류수정입력 >>>')
    db['posts'].update_one({'author' : name}, {'$set' : {'author' : data_author, 'title' : data_title, 'kind' : data_kind}})

    print('수정이 완료되었습니다. [수정 후 데이터 목록...]')
    for d in db['posts'].find():
        print(d)

except Exception as err:
    print('db수정에러발생 : ', err)
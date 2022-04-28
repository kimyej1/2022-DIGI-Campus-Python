# 23Book.py

import json

books = list()
books.append({"제목":"파이썬 정보", "출판년도":"2022", "출판사":"국민은행", "페이지":123, "가격":10000, "재고":True})
books.append({"제목":"핫브레이크", "출판년도":"1972", "출판사":"오리온", "페이지":48, "가격":3000, "재고":True})
books.append({"제목":"jelly bear", "출판년도":"2004", "출판사":"아트박스", "페이지":26, "가격":5000, "재고":False})
books.append({"제목":"JSON", "출판년도":"2017", "출판사":"DIGI", "페이지":66, "가격":15000, "재고":True})
books.append({"제목":"쉬는 시간", "출판년도":"1597", "출판사":"KB", "페이지":264, "가격":55000, "재고":False})

for book in books:
    print(book)

import json

with open("./book.json", "w", encoding="utf8") as f:
    json.dump(books, f)

with open("./book.json", "r", encoding="utf8") as f:
    readBooks = json.load(f)

print("=" * 30)

for book in readBooks:
    print(book)
    print(book["제목"])
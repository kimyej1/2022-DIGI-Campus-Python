# 10Book.py

books = list()  # list 이름 지을때는 '복수형'으로 지으면 편함
                # ex) for book in books: 이런식으로 활용하기 좋음

books.append({"제목":"파이썬 정복", "출판일":"2022", "출판사":"국민출판사", "가격":5000, "재고유무":True})
                # 출판일은 연, 연월, 연월일 등 형태가 다양할 수 있어서 일단 string 사용했습니다.
books.append({"제목":"자바월드", "출판일":"1990", "출판사":"한빛미디어", "가격":8000, "재고유무":False})
books.append({"제목":"프로그래밍", "출판일":"2002", "출판사":"소림사", "가격":33000, "재고유무":False})
books.append({"제목":"식권", "출판일":"1876", "출판사":"ABC", "가격":11000, "재고유무":True})
books.append({"제목":"WE WORK", "출판일":"2017", "출판사":"멀티캠퍼스", "가격":15000, "재고유무":False})
books.append({"제목":"스타뱅킹", "출판일":"2165", "출판사":"스뱅부", "가격":3500, "재고유무":True})
books.append({"제목":"스타뱅킹", "출판일":"2165", "출판사":"스뱅부", "가격":3500, "재고유무":True})

'''
print(books)
print(type(books))
print(type(books[0]))

for book in books:
    print(book)
'''

highPrice = list()  # 가격이 1만원 이상인 책
existBook = list()  # 재고 있는 책
publishList = set() # 현재 책 모두 (중복제거를 위해 Set으로)

for book in books:
    if book["가격"] >= 10000:
        highPrice.append((book["제목"],book["가격"]))
    if book["재고유무"] == True:
        existBook.append((book["제목"],book["재고유무"]))
    publishList.add((book["제목"], book["출판사"]))

print("highPrice : ", highPrice)
print("existBook : ", existBook)
print("publishList : ", publishList)

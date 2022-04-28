# 17Re.py

import re

text = "My ID is nadopro and passw123456-78-901234ord is 010-1234-5a789!@#&홍길동010-1234-5678이순신대한민국**(@&(d*!@(*ajdABChasjk1!"

# "A" 문자 찾기
print(re.findall("A", text))
result = re.findall("A", text)
print("result = ", result)

print(re.findall("[ABC]{2}", text))    # 010-[0-9]{4}-[0-9]{4} : 전화번호 찾기
print(re.findall("[가-힣]{3}", text))   # [가-힣]{3} : 3글자 이름 찾기
print(re.findall("010-[0-9]{4}-\d{4}", text))   # \d: 숫자, \D: 숫자 아닌거
print(re.findall("[@&(*!@(*]",text))
print(re.findall("\D",text))
print(re.findall("\S",text))

print(re.findall("[0-9]{6}-\d{2}-\d{6}", text))
print(re.findall("[a-z]+", text))

myList = re.findall("[@&(*!@(*]",text)
if len(myList) >= 1 :
    print("Find!!")
else:
    print("Not Found..")



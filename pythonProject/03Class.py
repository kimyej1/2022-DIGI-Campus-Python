# 03Class.py

var1 = "I am Python"
var2 = "I am Python"
print(id(var1))
print(id(var2))
print(var1 == var2)
print(var1 is var2)

var2 = "Hello Python"
print(id(var1))
print(id(var2))
print(var1 == var2)
print(var1 is var2)

var2 = 12
print("type of var1 = ", type(var1))
print("type of var2 = ", type(var2))

var1 = var1.replace("Python", "파이썬")
print(var1)

# 문자열형 데이터타입(str)
# 파이썬의 문자열은 "큰따옴표"도 되고 '작은따옴표'도 됩니다. \를 사용하라.
test = "파이썬의 문자열은 \"큰따옴표\"도 되고 '작은따옴표'도 됩니다. \를 사용하라."
print(test)
print("ABC",
      "DEF",
      "GHI")
test1 = "ABC" + "DEF" + "GHI"
test2 = "ABC" + "DEF" + "GHI" * 10
print(test1)
print(test2)

# test = "ABC" + 123
# print(test)

test = "대한민국"
len = len(test)
print("len = ", len)

str1 = "hello Python programming"
result = str1.startswith("Hello")
print(result)
result = str1.endswith("Program")
print(result)
result = str1.replace("Python", "JAVA")
print("replace : ", result)
result = str1.capitalize()   # 맨앞글자를 대문자로 쓰기
print("capitalize : ", result)
result = str1.upper()        # 대문자로 바꾸기
print("upper : ", result)
result = str1.isupper()      # 대문자인지 물어보기(T/F)
print("isUpper : ", result)
result = str1.find("JAVA")   # 몇번째 있는지 물어보기 : 못찾으면 무조건 -1(0부터 세니까!)
print("find1 : ", result)
result = str1.find("Python")
print("find2 : ", result)

result = "/".join(str1)
print(result)

print("123", 456)
print(int("123")+456)
print("123" + str(456))

f = 3.14
print(f)
print(type(f))

# d = double(3.14)

f = float(3)
print(f)
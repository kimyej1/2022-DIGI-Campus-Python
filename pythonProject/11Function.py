# 11Function.py

def foo():
    name = input("Insert name : ")
    print(name, "님, 반갑습니다.")

def bar():
    table = input("몇 단을 외울까요? ")
    print(table, "단...")

def sayHello(name):
    print("Hello Mr.",name)
    print("Nice to meet you.")

def add(a,b):
    return a + b
'''
foo()
bar()
sayHello("KIM")
sayHello("LEE")

value = add(1,2)
print("value = ", value)
'''
# 사용자로부터 두 값을 입력받는다.
# 11 + 22 = 33
'''
num1 = int(input("Insert num1 : "))
num2 = int(input("Insert num2 : "))
print(num1, "+", num2, "=", add(num1,num2))


def noReturn(name):
    if name == "KIM":
        print("안녕하세요.")
        return
    else:
        print("Hello.")

    print("Nice to see you.")
    return "OK"

ret = noReturn("KIM")
print(type(ret))
ret = noReturn("LEE")
print(type(ret))

def myRange(start = 0, end=0, step = 1):
    print("start = ", start, ", end = ", end, ", step = ", step)

myRange(10)
myRange(10,5)
myRange(10,5,3)
'''

# 가변 길이 인자
# * : tuple
# ** : dict
def introFamily(name, *familyNames, **familyInfo):
    print("내 이름은", name, "입니다.")
    print("가족의 이름은 다음과 같습니다.")
    for name in familyNames:
        print(name)
    for key in familyInfo.keys():
        print(key," : ", familyInfo[key])
    print("-" * 80)

introFamily("홍길동", "엄마", "아빠", "형", "동생", "할머니", 주소 = "서울", 가훈 = "투표하자") # 사람들마다 다를 수 있음
introFamily("이순신", "할머니", "할아버지", 위치 = "선릉")

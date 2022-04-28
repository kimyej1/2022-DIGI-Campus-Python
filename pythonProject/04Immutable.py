# 04Immutable.py
# Mutable (변할 수 있는), Immutable (변할 수 없는 : "불변객체")

# Mutable 예시 : int, str (매번 메모리가 변한다~)
a = "Hello"
print(id(a))
a = "World"
print(id(a))

b = 3
print(id(b))
b = 5
print(id(b))

myList = ["Hello"]      # List 형태 : [a, b, c]
print(myList)
print(type(myList))
print(id(myList))

myList[0] = "안녕하세요"
print(myList)           # 아까는 Hello였는데 내용 바뀜
print(type(myList))
print(id(myList))       # 메모리 위치 똑같음
                        # (매번 값이 바뀔때마다 List처럼 큰 덩어리의 메모리를 새로 할당하기 어려워서)

# 데이터 구조(Data Structure)
# 1. List : [ ]
lotto = [11, 22, 33, 44, 55, 66]
print(lotto)
print("type of lotto = ", type(lotto))
val0 = lotto[0]
print(val0)
val = lotto[-2]     # 음수색인 허용
print(val)

size = len(lotto)
print("size of lotto = ", size)
print(lotto[5])

lotto.append(77)
lotto.append(30)
print(lotto)

# remove(값) -- index를 주고 사용하지 않고 직접 값을 줘서 사용함
lotto.remove(33)    # 그러므로 remove를 할땐 그 값이 있는지부터 확인해야함
print(lotto)

lotto.insert(1, 333)      # 몇번째에 이 값을 넣어줘 (index, value)
print(lotto)              # 나머지 값은 뒤로 밀림

val = lotto.pop(4)              # 4번째 값을 빼(pop)라!
print("val = ", val)            # 4번째 값이 뭔지 확인 -> 55
print(lotto)

small = lotto[1:6]      # 엑셀에서 범위 지정할때 A1:B3 이렇게 쓰니까!
print(small)            # index 1 이상 6 미만 (1~5번째 자리)
print(lotto[1:4])       # index 1 이상 4 미만 (1~3번째 자리)

print(lotto)
clone = lotto           # 복제하기 ('='이란, 새로운 메모리 만드는게 아니라..)
clone.append(999)
print(lotto)            # clone에 999 더했는데 lotto에도 더해짐
                        # --> clone과 lotto는 "같은 메모리를 공유해"
print("id lotto = ", id(lotto))
print("id clone = ", id(clone))

copyList = lotto[:]        # 복제 말고 똑같은 새로운거 하나 만들고싶어
                           # [:] : 처음부터 끝까지!
copyList.append(1111)
print("lotto = ", lotto)
print("copyList = ", copyList)

print("id lotto = ", id(lotto))
print("id copyList = ", id(copyList))

# List 합치기..
a = [1,2,3]
b = [4,5,6]
print(a + b)

lang = ["Python", "C", "Java", "C++"]
print(lang)
lang.append(10)
lang.append(20)
print(lang)      # List에 숫자, 문자 혼용해서 들어갈 수 있다

# nested : 내포 (중첩) List
nest = [[1,2,3], [4,5,6], [7,8,9]]  # List안에 또 List
print(nest[1])
print(nest[-1])
print(nest[:])
print(nest[1][2])   # nest[1] list의 [2]

pgm = "Python Programming"
print(pgm[0])
print(pgm[0:7])
print(pgm[-3:])

# 빈 list 만드는 법 2가지 : empty list
emptyList = []      # ① 빈 대괄호 쓰기
print("emptyList = ", emptyList)
print("emptyList ID = ", id(emptyList))

empty = list()      # ② 자바 생성자처럼 만들기
print("empty = ", empty)
print("empty ID = ", id(empty))

# tuple : 쌍 (뭔가의 쌍으로 되어있는 데이터)
# 5 tuple : srcIP, srcPort, dstIP, dstPort, protocol(TCP/UDP) -- 이 다섯가지로 모든 데이터 구분 가능!

movie = "슈퍼맨", 1980, "배트맨", 1995, "오징어게임", 2021
print(movie)                 # 1. 대괄호가 아니라 소괄호가 묶고있음
print(movie[0])
print(movie[1])              # 2. List와 인덱스 순서, 길이가 똑같다
size = len(movie)
print("size = ", size)
print(type(movie))           # tuple 튜플!

table = [1,2,3], [4,5,6]     # 얘는 전체적으로 둘러싼 []가 없으므로 list 아님
                             # 기호가 아무것도 없으면 tuple로 처리한다
print(table)
print(type(table))
print(type(table[0]))
print(type(table[0][1]))

table[1][2] = 66
print(table)

# 빈 튜플 만들기 : empty tuple
emptyTuple = ()         # ① 빈 소괄호 쓰기
print(type(emptyTuple))
empty = tuple()         # ② 생성자처럼 만들기
print(type(empty))

myString = "Hello"
myTuple = "Hello",      # str과 tuple 구분: ,(끝의 쉼표)
print(type(myString))
print(type(myTuple))

print(movie)
a, b, c, d, e, f = movie # Unpacking 가능
print("c = ", c)

movieList = list(movie)
print(movieList)
print(type(movieList))

# Set : 집합 (유일하게 중복을 허용하지 않는 데이터 모임)
# A = {1,2,1,3,1,4,2,3,2,2} = {1,2,3,4}

lang = {"C", "C++", "Java", "C", "Python", "Java", "C++", "PHP", "C"}
print(lang)     # 알아서 중복 제거

a = set("samsungmulticampus")
b = set("kbstarmoonjaewoo")
print(a)
print(b)
print("a-b = ", a-b)  # a에만 있고 b에는 없는 것

# &&, and → a & b : 교집합 (Intersection)
# ||, or  → a | b : 합집합 (Union)
print("a&b = ", a&b)
print("a|b = ", a|b)
print("a^b = ", a^b)    # 합집합 - 교집합 (여집합)


# Dictionary Type
    # 다른 랭귀지에서는 map data / map type 이라고 하기도 함
    # 주로 대용량 데이터에서 사용
# key : value
# dict[apple], 사과

colors = {"RED":1, "BLUE":2, "YELLOW":3}
print(colors)
dict = {"apple":"사과", "desk":"책상", "note":"공책"}
print(dict)

# 연관배열 (associative array) - 첨자 대신에 문자열을 입력해서 해당 데이터를 찾아주는 배열
print(dict["apple"])    # 이렇게 사용한다

dict["phone"] = "전화기"
dict["book"] = "책"
print(dict)

print(list(dict.keys()))
print(sorted(dict.keys()))                 # key값 기준 오름차순 정렬
print(sorted(dict.keys(), reverse=True))   # key값 기준 내림차순 정렬

print(sorted(dict.values()))               # value값 기준 오름차순 정렬
print(sorted(dict.values(), reverse=True)) # value값 기준 내림차순 정렬
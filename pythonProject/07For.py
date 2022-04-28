# 07For.py

# Java : Enhanced For
# for(int valut : lotto)
#   System.out.println(value)
# colors = "black",

colors = "aaa", "bbb", "ccc", "xxx"
print(type(colors))
for color in colors:    # 이렇게 코딩하면, colors에 데이터가 늘어나도 for부분은 수정하지 않아도 됨
    print(color)

myList = list(range(10))
print(myList)

sum = 0

# 2의 배수만 더하기
for x in range(1,101):
    if x % 2 == 0:
        sum = sum + x       # 파이썬에는 ++, -- 없음, +=, -=는 있음!
        print("2 + 4 + 6 + .... + " , x)
    elif x % 3 == 0:
        print(x)
    else:
        print("xxx")
print("sum = ", sum)

# 사용자로부터 입력(table), 해당 단을 출력
# ex) 3 * 1 = 3
#     3 * 2 = 6
#     ...
#     3 * 9 = 27

table = input("구구단 몇단을 외울까요? : ")

for x in range(1, 10):
    print(table, "*", x, "=", int(table) * x)

# 1단부터 9단까지 다 외우기
for x in range(1,10):
    print("<", x, "단 >")
    for y in range(1,10):
        print(x, "*", y, "=", x * y)

print("-" * 80)

nest = [[1,2,3], [4,5,6], [11,22], [33], [44,55,66,77,88,99]]
#       nest[0], nest[1], nest[2]
# for문을 이용해서, 한줄에 하나씩 출력하시오.
# 출력 순서는 1,2,3,4,...33

for x in range(len(nest)):
    for y in range(len(nest[x])):
        print(nest[x][y])

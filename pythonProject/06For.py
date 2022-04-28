# 06For.py

# enhanced for(자바)
# for(int value : lotto) -- lotto에서 하나씩 순서대로 가져와서 value에 넣어라

colors = "red", "blue", "green", "yellow", "black"
size = len(colors)
print("size = ", size)

for color in colors:    # 'enhanced for'의 파이썬버전 -- colors에서 하나씩 순서대로 가져와서 color에 넣어라
    print(color)        # 위의 colors가 바뀌어도 for문은 수정할 필요 없음

print("-" * 80)

# range(5) : 0, 1, 2, 3, 4 -- 0 이상 5 미만까지
autoList = list(range(10))  # 0 ~ 9를 list로 만들어서 이름을 autoList라고 해줘~
print(autoList)

autoList = list(range(1,5)) # 1 ~ 4를 ..
print(autoList)

autoList = list(range(1,100,3)) # (start, end, step)
print(autoList)

sum = 0
for i in range(1,11):   # 1 ~ 10을 하나씩 순서대로 가져와서 i에 넣어라
    sum = sum + i
print(sum)

print("-" * 80)

# 사용자로부터 숫자를 입력받는다.
# 1부터 입력받은 수를 모두 출력하고, 합을 맨 마지막에 출력하시오.

sum = 0
number = input("Insert number : ")

for i in range(1, int(number) + 1):
    print(i)
    sum = sum + i
print("sum = ", sum)

print("-" * 80)

# 1부터 입력받은 수까지의 2의 배수이거나, 3의 배수를 모두 출력하시오.

for i in range(1, int(number) + 1):
    if (i % 2 == 0) or (i % 3 == 0):
        print(i)

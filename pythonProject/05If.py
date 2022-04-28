# 05If.py
# 제어문 : switch문이 없다.
#       cf) 자바에서 'break'는 while 또는 switch를 빠져나가기 위해 썼었음
# if, while, for, continue, pass
# if ~ elif (자바는 else if, 파이썬은 elif)

color = input("red or blue : ")

if color == "red":
    print("Stop !!")
elif color == "blue":
    print("Pass !!")
else:
    print("Unknown")

# 신호등의 색을 받는다.
# 빨간색이면 멈추세요.
# 파란색이면,
#       준비되었나요?(Y/N)
#       yes: 건너세요.
#       no: 다음에 건너세요.
# 빨/파 아니면 알수없는 색입니다.

color = input("Insert color : ")

if color == "red":
    print("멈추세요.")
elif color == "blue":
    ready = input("ready? : ")
    if ready == "yes":
        print("건너세요.")
    elif ready == "no":
        print("다음에 건너세요.")
else:
    print("알 수 없는 색입니다.")



color = input("신호등 색(red/blue) : ")

if color == "red":
    print("멈추세요.")
elif color == "blue":
    ready = input("준비되었나요?(yes/no) : ")
    if ready == "yes":
        print("건너세요.")
    elif ready == "no":
        print("다음에 건너세요.")
else:
    print("알 수 없는 색입니다.")
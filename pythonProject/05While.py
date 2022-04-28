# While:

counter = 0
color = ""
stopFlag = False    # 종료 신호

while stopFlag == False:
    color = input("red / blue : ")
    if color == "red":
        counter = counter + 1
        print("Stop !!")
    elif color == "blue":
        answer = input("yes / no : ")
        if answer == "yes":
            print("Pass !!")
            stopFlag = True     # break 효과
        else:
            counter = counter + 1
            print("Wait...")
    else:
        counter = counter + 1
        print("Unknown Color...")
print("Counter = ", counter)

# 21FileRead.py

file = open("./test.txt", "a", encoding="UTF8") # append 모드
file.write("HELLO File Write Test\n")

name = input("Insert name : ")
file.write("안녕하세요😃 " + name + "님, 반갑습니다.\n")

for x in range(100000):
    file.write((str(x+1) + "\n"))

file.close()

readFile = open("./test.txt", "rt", encoding="UTF8") # read text 모드 (text가 기본이라 "r" = "rt")
for line in readFile:
    print(line)

readFile.close()
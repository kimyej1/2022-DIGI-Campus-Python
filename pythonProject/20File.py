# 20File.py

# w: write mode(커서 맨앞), a: append mode(커서 맨뒤)
file = open("d:/fwrite.txt", "a", encoding="utf8")
file.write("Hello 111 국민은행 ★ 😁😁 韓字 123")

name = input("Insert Name : ")
message = "안녕하세요, " + name + "님! 반갑습니다."
result = file.write(message)
print("result = ", result)
# file.flush()  --> 여기까지 다 되기 전까지는 다음으로 넘어가지마!
file.close()

print("-" * 80)

for x in range(1500):
    try:
        f = open("d:/xxx/" + str(x) + ".txt", "w")    # d드라이브에 파일 1500개 만들어보기
    except IOError:
        print("Error : ", x)
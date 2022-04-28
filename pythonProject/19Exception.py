# 19Exception.py
import traceback


def exceptionTest():
    try:
        age = int(input("Insert Age : "))
        age = age + 1
        print("Next Year = ", age)
    except Exception as err:
        print("Exception !!!")
        traceback.print_exc()

# exceptionTest()
# exceptionTest()

def exceptionFile(path):
    try:
        fp = open(path, "r")    # 원래는 열었으면 반드시 닫아야함! (OS에서 1,024개까지만 열어줌)
    except IOError:
        print("Cannot Open File : ", path)
    else:
        print("File has ", len(fp.readlines()), "lines")
        fp.close()
    finally:                    # try든 except든 무조건 finally는 거침 (보통 파일 닫는걸 여기에 씀)
        print("End of File ...")

exceptionFile("d:/test.txt")
exceptionFile("./a.txt")
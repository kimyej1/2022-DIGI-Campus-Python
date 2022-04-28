# 12Fact.py
# 4! = 4 * 3 * 2 * 1
#    = 1 * .... * 4

def factorial(n):
    y = 1
    for x in range(1,n+1):
        y = y * x
    return y

def fact(n):
    '''
    multi line comment
    함수 등의 내용을 기술해준다.
    예) 파라미터: 양의 정수
       리턴: 팩토리얼 값
    '''
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

input = int(input("Insert Number : "))
print("result = ", factorial(input))

"""
print("-" * 80)
print("recursive = ", fact(input))
"""

print(fact.__doc__)
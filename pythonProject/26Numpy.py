# 26Numpy.py
# 넘파이 : 숫자해석에 특화

# (예) int8 - 1바이트짜리 숫자(-128 ~ 127), int16 - 2바이트짜리 숫자, int32, int64,..
#     uint8(unsigned int8) - '부호가 없는' int8(0 ~ 255)


import numpy as np

A = np.array( [ [1,2,3], [4,5,6] ])
print(A)
print(type(A))      # ndarray : n-dimension(n차원의) array
print(A.dtype)      # 타입?    int32 : 32bit짜리 숫자로 이루어짐
print(A.ndim)       # 몇차원?  2 : 2차원
print(A.shape)      # 형태?   (2,3) : 2행 3열
print(A.itemsize)   # 사이즈?  4 : 4Byte(= 32bit)
print(id(A))
print(A[0].data)

print(np.arange(3))         # range와 동일 : 0 이상 3 미만
# arange([start], stop, [,step], dtype = None)
# range(10)
print(np.arange(3.0))
print(np.arange(3, 10))     # range와 똑같이 동작함 : 3 이상 10 미만
print(np.arange(3, 10, 2))  # range와 동일 : 3 이상 10 미만 2칸씩

A = np.arange(3)            # 0, 1, 2 : int
print(A.dtype)              # int인데 4Byte(= 32bit)짜리 ~

A = np.linspace(0.0, 10.0, num = 5)
print(A)                    # 0부터 10까지 5구간으로 나눠라

x1 = np.logspace(0.1, 1, num = 10)
print(x1)

A = np.arange(15)
print(A)
A = np.arange(15).reshape(5,3)  # '5행 3열'로 모양 바꿔줘
print(A)
print(A.T)

# 산술 연산
# +, -, *, /, //, %, **
print(A ** 2)

# 관계 연산
# >, <, >=, <=, !=, ==
print(A < 5)
print(A % 2 == 0)

# 논리 연산
print( (A > 5).any() ) # .any : 만족시키는게 하나라도 있나?
print( (A > 0).all() ) # .all : 모두 만족시키나?

A = np.arange(10)
print(A[3])
print(A[-1])
print(A[:3])

A[:5] = 99
print(A)
print("-" * 80)

A = np.array([1,1,1,2,2,3,3,3,3,1,2,3])
print(np.unique(A))

A = np.arange(1, 46)
np.random.shuffle(A)
print(A)
A = np.sort(A)
print(A)
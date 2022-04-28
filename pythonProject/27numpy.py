# 27numpy.py
# numpy = numerical python

import numpy as np
'''
tmp = []                                    # temporary list (data * 2 한걸 넣으려고..)
data = [1,2,3,4,5, "Hello", [11,22,33]]     # list의 장점: 아무 type 다 붙일 수 있음(str, int, list...)
                                            # list의 단점: 커지면 뒤죽박죽 섞임 (해당 메모리를 하나씩 찾아야 하는 부담 ↑, 속도 ↓)

for x in data:                              # for문을 돌면 데이터가 많아질수록 계산횟수가 너무 많아짐
    tmp.append(x * 2)
print("tmp = ", tmp)

myArray = np.array([1,2,3,4,5])             # for 없이 할 수 없을까? → numpy!
print(myArray * 3)

# numpy : data, datatype으로 구분됨

a = [1,2,3]
b = [4,5,6]
# a + b = [5,7,9] 로 만들고싶으면,
# (1) a,b 길이가 같은지 확인, (2) for 돌면서 각 인덱스끼리 합, (3) 새로운 리스트에 append

na = np.array([1,2,3], float)
nb = np.array([4,5,6])
nc = na + nb
print("nc = ", nc)

nd = 3 * na + 2 * nb
print("nd = ", nd)
# 이렇게 numpy 이용하면 for 돌지 않고도 가능!
'''

print(np.arange(1,5,0.5)) # 1~5를 0.5마다 쪼개

aa = np.arange(10)        # 0~9 만들기
print("aa = ", aa)

# linspace, lagspace

a = np.linspace(0.0, 10.0)    # 0~10 포함해서 50개(default)로 나눠라
print(a)
a = np.linspace(0.0, 10.0, 5) # 5개로 나눠라
print(a)

a = np.arange(5)
b = np.arange(5)
z = np.sqrt(a**2 + b**2)      # square root
print("sqrt(a**2 + b**2) = ", z)  # 3: 루트9 + 루트9 = 루트18 = 4루트2 = 4.242....

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b))
print("vstack = ", c) # vertical stack

d = np.hstack((a,b))
print("hstack = ", d) # horizontal stack

a = np.arange(10)
print(a.shape)
print(a)
b = a.reshape((2,5))
print(b)

print(a>3)

a = np.random.uniform(10,50,10).reshape(2,5)
print("uniform = ", a)

a = np.array([0,10,20,30]).reshape(4,1)
b = np.array([0,1,2]).reshape(1,3)
print(a + b)

a = np.random.randint(1,45,100)
print("lotto = ", a)
a = np.arange(10)

norm = np.random.randn(5,5)
print(norm)

# binary file, text file
a = np.arange(12).reshape(3,4)
np.savetxt("d:/mytext.txt",a)
txt = np.loadtxt("d:/mytext.txt")
print("txt = ", txt)


# 08Pass.py

for x in range(1,11):
    if x % 2 == 0:
        pass
    else:
        print("odd")
    print("-")


squares = []
for x in range(10):
    squares.append(x**2)

for x in squares:
    print(x)        # squares가 수정되어도 for 수정 불필요

squares = [x**2 for x in range(10)]


pairs = []
A = ["aaa", "bbb", "ccc"]
B = ["ccc", "ddd", "aaa"]
# a, b의 서로 다른 쌍 만들기 (a != b일때 pairs append(x,y))
# (a,c) (a,d) -> 이런건 ok
# (a,a) (c,c) -> X

for a in A:
    for b in B:
        if a == b:
            pass
        else:
            pairs.append((a,b))
print(pairs)

pairs = []
for a in A:
    for b in B:
        if a != b:
            pairs.append((a,b))
print(pairs)
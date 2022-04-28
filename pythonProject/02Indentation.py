# 02Indentation.py
# {}로 블럭 결정하지 않는다.
# 들여쓰기로 한다(4).

# range(10) 은 range(0,10,1)이랑 완전 같음 (0이상 10미만 1칸씩)

for x in range(5):  # 0이상 5미만 1칸씩 증가
                    # Java: for(int x=0, x<5, x++) {
    print(x)
    print('위 수의 제곱 = ', x**2)
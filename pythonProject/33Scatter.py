# 33Scatter.py

import numpy as np
import matplotlib.pyplot as graph

N = 200
x = np.random.rand(N)         # 200개 랜덤숫자
y = np.random.rand(N)
colors = np.random.rand(N)    # 색도 랜덤
area = np.pi * (15 * np.random.rand(N))**2              # pi * r^2 = 0~15의 반지름을 가진 원 만들기!(파이알제곱)
graph.scatter(x, y, s = area, c = colors, alpha = 0.5)  # alpha : 투명도(0~1)
graph.grid(True)
graph.show()


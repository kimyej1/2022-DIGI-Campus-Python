# 34-3D.py

import numpy as np
import matplotlib.pyplot as graph

# 3D를 위한 import
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = graph.figure(figsize=(8, 8))
fig.suptitle("$f(x,y) = x^2 + y^2$", color = "#0000FF", fontsize = 20)
x = np.linspace(-5, 5, 7)
y = np.linspace(-5, 5, 7)
X, Y = np.meshgrid(x, y)    # mesh : 모든 선을 다 연결하는..
Z = X**2 + Y**2             # 3차원엔 Z축도 있다

ax2 = fig.add_subplot(111, projection = '3d')
surface = ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.RdPu)
fig.colorbar(surface)
ax2.set_title("surface")


graph.show()


N = 200
x = np.random.rand(N)         # 200개 랜덤숫자
y = np.random.rand(N)
colors = np.random.rand(N)    # 색도 랜덤
area = np.pi * (15 * np.random.rand(N))**2              # pi * r^2 = 0~15의 반지름을 가진 원 만들기!(파이알제곱)
graph.scatter(x, y, s = area, c = colors, alpha = 0.5)  # alpha : 투명도(0~1)
graph.grid(True)
# 35Contour.py
# Contour : 외곽선

import numpy as np
import matplotlib.pyplot as graph

# 3D를 위한 import
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = graph.figure(figsize=(8, 8))
fig.suptitle("$f(x,y) = x^2 + y^2$", color = "#0000FF", fontsize = 20)
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)    # mesh : 모든 선을 다 연결하는..
Z = X**2 + Y**2             # 3차원엔 Z축도 있다

ax3 = fig.add_subplot(111, projection = '3d')
surface = ax3.contour(X, Y, Z)
fig.colorbar(surface)
ax3.set_title("contour")


graph.show()
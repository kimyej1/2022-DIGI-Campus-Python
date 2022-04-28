# 30Curve.py

import numpy as np
import matplotlib.pyplot as graph

# x = np.arange(5)
x = np.linspace(-5, 5, 100)   # 0~5를 50개로 나눠
y = x**2 - 1

graph.xlabel("x axis")
graph.ylabel("y won")
graph.title("Plot Math Function")
graph.grid(True)

graph.plot(x, y, "b-")
graph.show()
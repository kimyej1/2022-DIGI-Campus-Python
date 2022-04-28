# 31Sin.py

import numpy as np
import matplotlib.pyplot as graph

# x = np.arange(5)
x = np.linspace(0, 2 * np.pi, 100)   # pi = 3.14, 2 * np.pi = 6.24 (각도로는 180도, 2 * np.pi 이므로 360도)
y = np.sin(x)

graph.xlabel("x axis")
graph.ylabel("y won")
graph.title("y = sin(x)")
graph.grid(True)
line = graph.plot(x, y)                                 # 나중에 line만 불러와서 쓰려고
xmin, xmax, ymin, ymax = np.amin(x), np.amax(x), -1, 1  # 화면을 끝까지 꽉차게 쓰고싶어 → x, y의 최소/최대값 지정
graph.axis([xmin, xmax, ymin, ymax])
graph.plot([xmin, xmax], [0,0], color = 'blue', linewidth = 4.0)
graph.setp(line, color = 'red', linewidth = 2.0)

# graph.plot(x, y, "b-")
graph.show()
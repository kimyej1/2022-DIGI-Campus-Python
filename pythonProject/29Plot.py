# 29Plot.py

import matplotlib.pyplot as graph      # terminal에서 pip install matplotlib (설치 먼저!)
import numpy as np

x = np.arange(5) # [0,1,2,3,4]
y = np.arange(5) # [0,1,2,3,4]

graph.plot(x+1, y+5, "c-", x+10, y+20, "md")
# 색 → b : blue, r : red, m : magenta, g : green, y : yellow, c : cyan
# 모양(marker) → o : circle, 8: octagon, p : pentagon, D : diamond,
#               s : square, * : star, x : x모양, d : thin diamond, ^ v < > (상하좌우)


graph.xlabel("x")
graph.ylabel("y")
graph.title("Plot Line Marker")
graph.grid(True)                       # 그리드 보이게 해줘
graph.savefig("d:/plot_marker.png")    # 저장도 해줘(save figure)
graph.show()
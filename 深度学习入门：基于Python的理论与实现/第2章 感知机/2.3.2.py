# 将实现方式变为矩阵方式。

import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

print(w * x)
print(np.sum(w * x))
print(np.sum(w * x) + b)
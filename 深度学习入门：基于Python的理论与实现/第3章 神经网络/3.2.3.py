import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
  return np.array(x > 0, dtype=np.int64)

x = np.arange(-5, 5, 0.1)
y = step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1) # 指定x轴的范围
plt.show()
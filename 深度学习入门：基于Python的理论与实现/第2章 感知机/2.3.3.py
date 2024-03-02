# 权重 + 偏置实现
# AND，NAND，OR只是w和b不同，其他都一样

import numpy as np

def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum(x * w) + b
  if tmp <= 0:
    return 0
  elif tmp > 1:
    return 1

def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5]) # 仅权重和偏置和AND不同
  b = 0.7
  tmp = np.sum(x * w) + b
  if tmp <= 0:
    return 0
  elif tmp > 1:
    return 1

def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5]) # 仅权重和偏置和AND不同
  b = -0.2
  tmp = np.sum(x * w) + b
  if tmp <= 0:
    return 0
  elif tmp > 1:
    return 1
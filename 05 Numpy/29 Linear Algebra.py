#Author: Tonmoy M
#URL: https://qinetique.github.io

import numpy as np
np.set_printoptions(legacy="1.13")
N = int(input())
array = np.array([input().split() for i in range(N)], float)
print(np.linalg.det(array))
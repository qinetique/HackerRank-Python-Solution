#Author: Tonmoy M
#URL: https://qinetique.github.io

import numpy as np
np.set_printoptions(legacy="1.13")
N,M = map(int, input().split())
print(np.eye(N,M))
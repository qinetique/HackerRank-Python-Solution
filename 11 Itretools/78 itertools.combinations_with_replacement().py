#Author: Tonmoy M
#URL: https://qinetique.github.io

from itertools import *

S,N = input().split()
S = sorted(S)
N = int(N)
for i in combinations_with_replacement(S, N):
    print("".join(i))
#Author: Tonmoy M
#URL: https://qinetique.github.io

from itertools import combinations

S,N = input().split()
S = sorted(S)
N = int(N) + 1
for i in range(1, N):
    for j in combinations(S, i):
        print(''.join(j))

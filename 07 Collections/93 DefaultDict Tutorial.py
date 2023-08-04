#Author: Tonmoy M
#URL: https://qinetique.github.io

from collections import defaultdict

dfault = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    wr = input()
    dfault[wr].append(str(i+1))
for j in range(m):
    wr  =input()
    print(' '.join(dfault[wr]) or -1)
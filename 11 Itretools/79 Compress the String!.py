#Author: Tonmoy M
#URL: https://qinetique.github.io
import itertools

S = input().strip()
suck_em = list(set(S))
g = []
k = []

for a, b in itertools.groupby(S):
    g.append(list(b))
    k.append(a)
for i in range(len(g)):
    g_len = len(g[i])
    a = int(k[i])
    print((g_len,a), end=" ")
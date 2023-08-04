#Author: Tonmoy M
#URL: https://qinetique.github.io
import itertools

S,N = list(map(str, input().split(" ")))
S = sorted(S)
for x in list(itertools.permutations(S, int(N))):
    print(''.join(x))

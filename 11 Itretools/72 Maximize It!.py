#Author: Tonmoy M
#URL: https://qinetique.github.io
import itertools

K, M = map(int, input().split())
gud = []
for i in range(K):
    no_gud = list(map(int, input().split()))
    gud.append(no_gud[1:])
combine_guds = itertools.product(*gud)
dhon = 0
for single_gud in combine_guds:
    dhon = max(sum(x * x for x in single_gud) % M, dhon)
print(dhon)

#Author: Tonmoy M
#URL: https://qinetique.github.io
import itertools

dhon = list(map(int, input().split()))
gud = list(map(int, input().split()))
sex = list(itertools.product(dhon, gud))
for x in sex:
    print(x, end=" ")
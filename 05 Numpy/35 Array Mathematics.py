#Author: Tonmoy M
#URL: https://qinetique.github.io

import numpy
N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)
for i in range(N):
    temp = list(map(int, input().split()))
    B.append(temp)
npA = numpy.array(A)
npB = numpy.array(B)

print(npA + npB)
print(npA - npB)
print(npA * npB)
print(npA // npB)
print(npA % npB)
print(npA ** npB)

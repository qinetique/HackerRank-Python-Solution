#Author: Tonmoy M
#URL: https://qinetique.github.io
import numpy

ar = list(map(int, input().split()))
intr = tuple(ar)
print(numpy.zeros(intr, dtype=int))
print(numpy.ones(intr, dtype=int))
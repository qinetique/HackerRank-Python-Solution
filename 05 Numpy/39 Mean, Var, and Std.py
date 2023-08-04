#Author: Tonmoy M
#URL: https://qinetique.github.io
import numpy

N, M = map(int, input().split())
fuckin_arr = []
for i in range(N):
    temp = list(map(int, input().split()))
    fuckin_arr.append(temp)
fuckin_np = numpy.array(fuckin_arr)
print(numpy.mean(fuckin_np, axis=1))
print(numpy.var(fuckin_np, axis=0))
print(round(numpy.std(fuckin_np, axis=None), 11))

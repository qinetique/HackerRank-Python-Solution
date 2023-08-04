#Author: Tonmoy M
#URL: https://qinetique.github.io
import numpy

N, M = map(int, input().split())
fuckin_arr = []
for i in range(N):
    temp = list(map(int, input().split()))
    fuckin_arr.append(temp)
fuckin_np = numpy.array(fuckin_arr)
print(numpy.max(numpy.min(fuckin_np, axis=1)))

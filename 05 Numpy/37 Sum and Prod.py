#Author: Tonmoy M
#URL: https://qinetique.github.io
import numpy

N, M = map(int, input().split())
fuckin_arr = []
for i in range(N):
    temp = list(map(int, input().split()))
    fuckin_arr.append(temp)
fuckin_npa = numpy.array(fuckin_arr)
fuckin_np = numpy.sum(fuckin_arr, axis = 0)
print(numpy.prod(fuckin_np))

#Author: Tonmoy M
#URL: https://qinetique.github.io
import numpy

N, M = map(int, input().split())
fucking_array = []
for _ in range(N):
    fuckin_row = list(map(int,input().split()))
    fucking_array.append(fuckin_row)
numpy_array = numpy.array(fucking_array)
print(numpy.transpose(numpy_array))
print(numpy_array.flatten())
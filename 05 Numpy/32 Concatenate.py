#Author: Tonmoy M
#URL: https://qinetique.github.io
import numpy

N,M,P = map(int, input().split())
fuckin_array_one = []
fuckin_array_two = []
for i in range(N):
    fuckin_temporary = list(map(int, input().split()))
    fuckin_array_one.append(fuckin_temporary)
for i in range(M):
    fuckin_temporary = list(map(int, input().split()))
    fuckin_array_two.append(fuckin_temporary)
numpy_fuckin_one = numpy.array(fuckin_array_one)
numpy_fuckin_two = numpy.array(fuckin_array_two)

print(numpy.concatenate((numpy_fuckin_one, numpy_fuckin_two), axis = 0))
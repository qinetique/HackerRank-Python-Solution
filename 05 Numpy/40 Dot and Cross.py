#Author: Tonmoy M
#URL: https://qinetique.github.io
import numpy

N = int(input())
array_01 = []
array_02 = []
for i in range(N):
    temp = list(map(int, input().split()))
    array_01.append(temp)
num_ar = numpy.array(array_01)
for i in range(N):
    temp = list(map(int, input().split()))
    array_02.append(temp)
num_arr = numpy.array(array_02)
print(numpy.dot(num_ar, num_arr))

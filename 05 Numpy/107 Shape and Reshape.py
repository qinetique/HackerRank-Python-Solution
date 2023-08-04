#Author: Tonmoy M
#URL: https://qinetique.github.io
import numpy

latest_dhon = list(map(int, input().split()))
array_dhon = numpy.array(latest_dhon)
print(numpy.reshape(array_dhon, (3,3)))
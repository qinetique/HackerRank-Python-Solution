#Author: Tonmoy M
#URL: https://qinetique.github.io

from collections import namedtuple

N = int(input())
Student = namedtuple("Student", input())
res = sum([int(Student(*input().split()).MARKS) for i in range(N)]) / N
print("{:0.2f}".format(res))
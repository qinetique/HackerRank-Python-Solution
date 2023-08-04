#Author: Tonmoy M
#URL: https://qinetique.github.io

in_A = int(input())
setA = set(map(int, input().split()))

itr = int(input())
for i in range(itr):
    opr = input().split()
    create = set(map(int,input().split()))
    eval("setA.{}({})".format(opr[0],create))
print(sum(setA))
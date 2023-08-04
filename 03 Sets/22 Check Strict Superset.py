#Author: Tonmoy M
#URL: https://qinetique.github.io

setA = set(map(int, input().split()))
exSet = int(input())
strSupper = True

for i in range(exSet):
    exSetEx = set(map(int,input().split()))
    if not setA.issuperset(exSetEx):
        strSupper = False
print(strSupper)
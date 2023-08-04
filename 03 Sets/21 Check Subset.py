#Author: Tonmoy M
#URL: https://qinetique.github.io

testcases = int(input())
for i in range(testcases):
    setA = int(input())
    solSetA = set(map(int, input().split()))
    setB = int(input())
    solSetB = set(map(int, input().split()))
    print(solSetA.issubset(solSetB))
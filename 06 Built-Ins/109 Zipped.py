#Author: Tonmoy M
#URL: https://qinetique.github.io

N, X = map(int, input().split())
sc = []
for i in range(X):
    sc.append(list(map(float, input().split())))
for j in zip(*sc):
    print(sum(j) / len(j))
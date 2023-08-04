#Author: Tonmoy M
#URL: https://qinetique.github.io

N = int(input())
my_S = set()
for i in range(N):
    name = input()
    my_S.add(name)
print(len(my_S))
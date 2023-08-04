#Author: Tonmoy M
#URL: https://qinetique.github.io

n = int(input())
s = set(map(int, input().split()))
num = int(input())

for i in range(num):
    set1 = input().split()
    if set1[0] == "pop":
        s.pop()
    elif set1[0] == "remove":
        s.remove(int(set1[1]))
    elif set1[0] == "discard":
        s.discard(int(set1[1]))
print(sum(s))
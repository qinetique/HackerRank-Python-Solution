#Author: Tonmoy M
#URL: https://qinetique.github.io
import collections

N = int(input())
d = collections.deque()

for i in range(N):
    a = list(input().split())
    test = a[0]
    if test == "append":
        d.append(int(a[1]))
    elif test == "appendleft":
        d.appendleft(int(a[1]))
    elif test == "pop":
        d.pop()
    elif test == "popleft":
        d.popleft()
for i in d:
    print(i, end=' ')
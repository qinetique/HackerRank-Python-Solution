#Author: Tonmoy M
#URL: https://qinetique.github.io
from collections import deque

fuckin_case = int(input())
for i in range(fuckin_case):
    n = int(input())
    d = deque(map(int, input().split()))
    con = True
    sn = (2**31) + 1
    while d:
        left_sn = d[0]
        right_sn = d[-1]
        if left_sn >= right_sn and sn >= left_sn:
            sn = d.popleft()
        elif left_sn <= right_sn and sn >= right_sn:
            sn = d.pop()
        else:
            con = False
            break
    if con:
        print("Yes")
    else:
        print("No")

#Author: Tonmoy M
#URL: https://qinetique.github.io

X = int(input())
dhon_size = list(map(int, input().split()))
N = int(input())
sell_dhon = 0
for i in range(N):
    a, b = map(int, input().split())
    if a in dhon_size:
        sell_dhon = sell_dhon + b
        dhon_size.remove(a)
print(sell_dhon)
#Author: Tonmoy M
#URL: https://qinetique.github.io
from re import match, compile

N = int(input())
for i in range(N):
    number = input()
    con = compile(r"^[7-9]\d{9}$")
    if bool(match(con, number)):
        print("YES")
    else:
        print("NO")
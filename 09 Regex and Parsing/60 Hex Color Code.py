#Author: Tonmoy M
#URL: https://qinetique.github.io
import email.utils
import re

N = int(input())
for i in range(N):
    css = input()
    soln = re.findall(r"(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})", css)
    for j in soln:
        if j != "":
            print(j)
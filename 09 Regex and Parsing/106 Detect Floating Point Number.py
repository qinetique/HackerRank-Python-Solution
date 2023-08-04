#Author: Tonmoy M
#URL: https://qinetique.github.io
from re import compile, match

rgx = compile("^[-+]?\d*\.\d+$")
for i in range(int(input())):
    print(bool(rgx.match(input())))
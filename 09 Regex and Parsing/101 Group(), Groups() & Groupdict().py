#Author: Tonmoy M
#URL: https://qinetique.github.io
import re

S = input()
soln = re.search(r"([A-Za-z0-9])\1", S)
if soln is None:
    print(-1)
else:
    print(soln[1])
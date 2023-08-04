#Author: Tonmoy M
#URL: https://qinetique.github.io
import re

S = input().strip()
k = input().strip()
sex_length = len(S)
fuck = False
for i in range(sex_length):
    soln = re.match(k,S[i:])
    if soln:
        sex_index = i + soln.start()
        sex_end = i + soln.end() - 1
        print((sex_index, sex_end))
        fuck = True

if fuck == False:
    print("(-1, -1)")
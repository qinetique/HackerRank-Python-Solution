#Author: Tonmoy M
#URL: https://qinetique.github.io
import re

S = input()
soln = re.findall(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])", S)
if soln:
    for i in soln:
        print(i)
else:
    print(-1)
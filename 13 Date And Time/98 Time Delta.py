#Author: Tonmoy M
#URL: https://qinetique.github.io

import datetime
x = int(input())
t_format = "%a %d %b %Y %H:%M:%S %z"
for i in range(x):
    tstmp01 = input().strip()
    tstmp02 = input().strip()
    tsec01 = datetime.datetime.strptime(tstmp01, t_format)
    tsec02 = datetime.datetime.strptime(tstmp02, t_format)
    print(int((abs(tsec01 - tsec02).total_seconds())))
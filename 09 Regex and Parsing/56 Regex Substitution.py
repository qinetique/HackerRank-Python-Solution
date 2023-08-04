#Author: Tonmoy M
#URL: https://qinetique.github.io
import re
import sys

N = int(input())
for line in sys.stdin:
    r_and = re.sub(r"(?<= )(&&)(?= )", "and", line)
    r_or = re.sub(r"(?<= )(\|\|)(?= )", "or", r_and)
    print(r_or, end="")
#Author: Tonmoy M
#URL: https://qinetique.github.io
from collections import Counter

#this can be solved by two methods
# 1. Counter Functions
# 2. Lambda Expression
# I will go for counter function.

if __name__ == '__main__':
    s = input()
    s = sorted(s)
    frq = Counter(list(s))

    for a, b in frq.most_common(3):
        print(a,b)
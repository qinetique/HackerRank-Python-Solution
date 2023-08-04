#Author: Tonmoy M
#URL: https://qinetique.github.io

from collections import Counter, OrderedDict
class CountOrder(Counter, OrderedDict):
    pass
arr = []
n = int(input())
for i in range(n):
    arr.append(input().strip())
count_word = CountOrder(arr)
print(len(count_word))
for i in count_word:
    print(count_word[i], end=" ")
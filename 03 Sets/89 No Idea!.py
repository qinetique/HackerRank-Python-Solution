#Author: Tonmoy M
#URL: https://qinetique.github.io
from collections import Counter

n,m = map(int, input().split())
data = list(map(int, input().split()))
count_data = Counter(data)
set_data = set(data)
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
moodoff = 0
for i in set_data & set_a:
    moodoff += count_data[i]
for i in set_data & set_b:
    moodoff -= count_data[i]
print(moodoff)
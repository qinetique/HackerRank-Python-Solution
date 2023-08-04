#Author: Tonmoy M
#URL: https://qinetique.github.io
import collections
import re

N = int(input())
its = collections.OrderedDict()
for i in range(N):
    r_lst = re.split(r"(\d+)$", input().strip())
    item_name = r_lst[0]
    net_price = int(r_lst[1])
    if item_name not in its:
        its[item_name] = net_price
    else:
        its[item_name] = its[item_name] + net_price
for i in its:
    print(f'{i}{its[i]}')
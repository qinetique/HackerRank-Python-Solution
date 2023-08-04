#Author: Tonmoy M
#URL: https://qinetique.github.io

from itertools import combinations

n = int(input())
arr = input().split()
k = int(input())
mk_list = list(combinations(arr, k))
fn_list = [x for x in mk_list if "a" in x]
print(len(fn_list)/len(mk_list))
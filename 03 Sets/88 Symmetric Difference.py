#Author: Tonmoy M
#URL: https://qinetique.github.io

M = int(input())
d_set = set(map(int, input().split()))
N = int(input())
g_set = set(map(int, input().split()))

diff_d_set = d_set.difference(g_set)
diff_g_set = g_set.difference(d_set)
for i in sorted(diff_d_set.union(diff_g_set)):
    print(i)
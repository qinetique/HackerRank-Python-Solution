#Author: Tonmoy M
#URL: https://qinetique.github.io

k = int(input())
r_num_lst = list(map(int,input().split()))
r_num_set = set(r_num_lst)
total_r_num = sum(r_num_lst)
total_r_set = sum(r_num_set) * k
fuckoff = total_r_set - total_r_num

for i in r_num_set:
    if fuckoff == (k - 1)* i:
        print(i)
        break
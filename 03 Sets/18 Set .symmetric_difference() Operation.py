#Author: Tonmoy M
#URL: https://qinetique.github.io

st_eng = int(input())
st_roll_eng = set(map(int, input().split()))
st_fr = int(input())
st_roll_fr = set(map(int, input().split()))
o_subs = st_roll_eng.symmetric_difference(st_roll_fr)
print(len(o_subs))
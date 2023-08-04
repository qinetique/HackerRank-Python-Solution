#Author: Tonmoy M
#URL: https://qinetique.github.io
import email.utils
import re

n = int(input())
for i in range(n):
    em = input()
    ck_email = email.utils.parseaddr(em)[1].strip()
    fuckin_solve = bool(re.match(r"(^[A-Za-z][A-Za-z0-9\._-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$", ck_email))
    if fuckin_solve:
        print(em)
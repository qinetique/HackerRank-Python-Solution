#Author: Tonmoy M
#URL: https://qinetique.github.io

import re

n = int(input())
for i in range(n):
    s = input().strip()
    rgx = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',s)
    if rgx:
        ps = ''.join(rgx.group(0).split('-'))
        fuckin_mind = re.search(r'(\d)\1{3,}', ps)
        if fuckin_mind:
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
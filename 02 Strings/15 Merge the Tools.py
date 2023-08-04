#Author: Tonmoy M
#URL: https://qinetique.github.io
import re


def merge_the_tools(string, k):
    # your code goes here
    tonmoy = []
    tonmoy = re.findall("[A-Z]{0,%s}" %k, string)

    for i in range(len(tonmoy)):
        gud = sorted(set(tonmoy[i]), key=tonmoy[i].index)
        gud = "".join(gud)
        print(gud)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
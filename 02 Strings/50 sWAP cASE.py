#Author: Tonmoy M
#URL: https://qinetique.github.io

def swap_case(s):
    fuckedup_s = ""
    for c in s:
        if c.isupper():
            fuckedup_s += c.lower()
        elif c.islower():
            fuckedup_s += c.upper()
        else:
            fuckedup_s += c
    return fuckedup_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
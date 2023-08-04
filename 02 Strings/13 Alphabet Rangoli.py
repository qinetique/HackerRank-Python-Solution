import string
#Author: Tonmoy M
#URL: https://qinetique.github.io

infolk = string.ascii_lowercase
def print_rangoli(size):
    #GUD
    tonmoy = []
    for r in range(size):
        t_print = "-".join(infolk[r:size])
        tonmoy.append(t_print[::-1] + t_print[1:])
    fuck = len(tonmoy[0])

    for r in range(size - 1, 0 , -1):
        print(tonmoy[r].center(fuck,"-"))

    for r in range(size):
        print(tonmoy[r].center(fuck, "-"))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
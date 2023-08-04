#Author: Tonmoy M
#URL: https://qinetique.github.io
def minion_game(string):
    # your code goes here
    tonmoy = "AEIOU"
    a = 0
    b = 0
    for i in range(len(string)):
        if string[i] in tonmoy:
            a += len(string) -i
        else:
            b += len(string) - i
    if a > b:
        print("Kevin", a)
    elif b > a:
        print("Stuart", b)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
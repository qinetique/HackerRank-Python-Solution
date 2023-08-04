#Author: Tonmoy M
#URL: https://qinetique.github.io

def print_formatted(number):
    for i in range(1, number + 1):
        a = len(f"{number:b}")
        print(f"{i:{a}} {i:{a}o} {i:{a}X} {i:{a}b}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Author: Tonmoy M
#URL: https://qinetique.github.io

if __name__ == '__main__':
    x,k = map(int, input().split())
    eqn = input().strip()
    print(eval(eqn) == k)
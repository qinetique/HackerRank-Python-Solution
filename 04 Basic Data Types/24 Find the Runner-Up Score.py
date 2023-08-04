#Author: Tonmoy M
#URL: https://qinetique.github.io


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    anArray = list(set(arr))
    anArray.sort()
    print(anArray[-2])
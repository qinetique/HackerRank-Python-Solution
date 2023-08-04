#Author: Tonmoy M
#URL: https://qinetique.github.io

def average(array):
    # your code goes here
    sexy_heights = set(array)
    bal_height = sum(sexy_heights)/len(sexy_heights)
    return round(bal_height,3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
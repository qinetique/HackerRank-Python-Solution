#Author: Tonmoy M
#URL: https://qinetique.github.io

cube = lambda x: x * x * x # complete the lambda function

def fibonacci(n):
    arr = [0,1]
    if n < 2:
        return arr[:n]
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
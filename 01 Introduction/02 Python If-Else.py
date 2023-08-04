#Author: Tonmoy M
#URL: https://qinetique.github.io

if __name__ == "__main__":
    n = int(input().strip())
    #condition goes here
    if n % 2 == 1 or 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
#Author: Tonmoy M
#URL: https://qinetique.github.io


if __name__ == '__main__':
    N = int(input())
    fuckin_array = []
    for i in range(N):
        c_args = input().split(" ")
        a = c_args[0]
        if a == "print":
            print(fuckin_array)
        elif a == "sort":
            fuckin_array.sort()
        elif a == "insert":
            playstation = int(c_args[1])
            bal_er_value = int(c_args[2])
            fuckin_array.insert(playstation, bal_er_value)
        elif a == "remove":
            bal_er_value = int(c_args[1])
            fuckin_array.remove(bal_er_value)
        elif a == "append":
            bal_er_value = int(c_args[1])
            fuckin_array.append(bal_er_value)
        elif a == "pop":
            fuckin_array.pop()
        elif a == "reverse":
            fuckin_array.reverse()
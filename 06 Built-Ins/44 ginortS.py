#Author: Tonmoy M
#URL: https://qinetique.github.io

S = input()

#solved by lambda expression

print(''.join(sorted(
    S, key=lambda x:(
        x.isdigit() and int(x) % 2 == 0,
        x.isdigit(),
        x.isupper(),
        x.lower(),
        x,
    ),
)))
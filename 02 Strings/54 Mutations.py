#Author: Tonmoy M
#URL: https://qinetique.github.io

def mutate_string(string, position, character):
    fuckin_chars = list(string)
    fuckin_chars[position] = character
    return ''.join(fuckin_chars)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
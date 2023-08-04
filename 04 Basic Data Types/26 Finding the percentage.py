#Author: Tonmoy M
#URL: https://qinetique.github.io


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #2 line er code er jnno gud maramari
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:0.2f}")

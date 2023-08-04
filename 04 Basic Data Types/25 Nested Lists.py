#Author: Tonmoy M
#URL: https://qinetique.github.io


if __name__ == '__main__':
    fucking_students = []
    fucking_scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        fucking_students.append(student)
        fucking_scores.append(score)
    min_score = sorted(set(fucking_scores))[1]
    fuckers_names = sorted(
        [student[0] for student in fucking_students if student[1] == min_score]
    )
    print("\n".join(fuckers_names))

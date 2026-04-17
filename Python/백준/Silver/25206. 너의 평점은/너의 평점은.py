import sys
input = sys.stdin.readline

trans_grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade_index = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']

sum = 0.0
credit = 0.0

for i in range(20):
    name, score, grade = input().split()
    score = float(score)

    for j in range(len(grade_index)):
        if grade == grade_index[j]:
            sum += (score * trans_grade[j])
            credit += score

print(sum / credit)
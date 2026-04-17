import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    student = list(input().split())
    
    for i in range(1, 4):
        student[i] = int(student[i])

    students.append(student)

students = sorted(students, key= lambda x: (x[3], x[2], x[1]))

print(students[-1][0])
print(students[0][0])
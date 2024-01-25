import sys
input = sys.stdin.readline

N = int(input())
grades = []

for i in range(N):
    name, korean, english, math = map(str, input().split())
    korean = int(korean)
    english = int(english)
    math = int(math)

    grades.append([name, korean, english, math])

grades.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for j in range(N):
    print(grades[j][0])
import sys
input = sys.stdin.readline

join = []

N = int(input())

for i in range(N):
    age, name = input().split()
    join.append([int(age), i, name])

join.sort(key=lambda x: (x[0], x[1]))

for m in join:
    print(m[0], m[2])
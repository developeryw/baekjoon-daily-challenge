import sys
input = sys.stdin.readline

toy = list(input().strip() for _ in range(5))

for k in range(0, 5, 1):
    if len(toy[k]) < 15:
        toy[k] += ' ' * (15 - len(toy[k]))

for i in range(0, 15, 1):
    for j in range(0, 5, 1):
        if toy[j][i] != ' ':
            print(toy[j][i], end="")
import sys
input = sys.stdin.readline

T = int(input())
score = []

for i in range(T):
    arr = str(input())
    O = 0
    total = 0

    for j in range(0, len(arr)):
        if arr[j] == 'O':
            O += 1
            total += O
        elif arr[j] == 'X':
            O = 0

    score.append(total)

for s in score:
    print(s)
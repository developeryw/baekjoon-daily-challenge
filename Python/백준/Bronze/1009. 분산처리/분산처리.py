import sys
input = sys.stdin.readline

computer = {1: [1], 2: [6, 2, 4, 8], 3: [1, 3, 9, 7],
            4: [6, 4], 5: [5], 6: [6], 7: [1, 7, 9, 3],
            8: [6, 8, 4, 2], 9: [1, 9]}

T = int(input())
result = []

for i in range(T):
    a, b = map(int, input().split())
    a = a % 10

    if a in computer:
        answer = computer[a][b % len(computer[a])]
    else:
        answer = 10
        
    result.append(answer)

print(*result, sep="\n")
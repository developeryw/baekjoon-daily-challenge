import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
i = 0
j = 0
total = 0
result = 0

while True:
    if total >= M:
        total -= A[i]
        i += 1
    elif j == N:
        break
    else:
        total += A[j]
        j += 1

    if total == M:
        result += 1

print(result)
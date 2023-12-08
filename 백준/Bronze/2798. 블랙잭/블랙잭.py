import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = list(map(int, input().split()))
maximum = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            num = number[i] + number[j] + number[k]
            if num <= M:
                maximum = max(maximum, num)

print(maximum)
import sys
input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))

T.sort(reverse=True)

days = 0

for i in range(N):
    if T[i] + i > days:
        days = T[i] + i

print(days + 2)
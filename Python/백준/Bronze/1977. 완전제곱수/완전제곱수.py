import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

total = 0
minimum = 100000000

for i in range(M, N+1):
    if i ** 0.5 - int(i ** 0.5) == 0:
        total += i
        minimum = min(minimum, i)

if total == 0:
    print(-1)
else:
    print(total)
    print(minimum)
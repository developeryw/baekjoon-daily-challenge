import sys
input = sys.stdin.readline

N = int(input())
stick = []
cur = 0
result = 0

for _ in range(N):
    h = int(input())
    stick.append(h)

for _ in range(N):
    tmp = stick.pop()

    if tmp > cur:
        cur = tmp
        result += 1

print(result)
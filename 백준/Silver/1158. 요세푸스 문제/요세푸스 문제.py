import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
circle = [i for i in range(N)]
circle = deque(circle)
result = []

for j in range(N):
    for k in range(K-1):
        tmp = circle.popleft()
        circle.append(tmp)
    temp = circle.popleft()
    result.append(temp + 1)

print('<', end="")
print(*result, sep=", ", end="")
print('>')
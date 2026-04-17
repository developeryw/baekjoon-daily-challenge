import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
balloons = list(map(int, input().split()))

for i in range(N):
    balloons[i] = [balloons[i], i+1]

dq = deque(balloons)

result = []

while dq:
    cur = dq.popleft()
    result.append(cur[1])
    
    idx = cur[0]

    if idx > 0:
        dq.rotate(-idx + 1)
    else:
        dq.rotate(-idx)

print(*result)
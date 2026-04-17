import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
result = []

def queue_instruction(n, k):
    for i in range(1, n+1):
        queue.append(i)

    for j in range(n):
        queue.rotate(-k+1)
        result.append(queue.popleft())

    return 1

queue_instruction(N, K)

print('<', end='')
for r in result:
    if r != result[-1]:
        print(r, end=', ')
    else:
        print(r, end=">")
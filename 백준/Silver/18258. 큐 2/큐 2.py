import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
result = []

def queue_instruction(args):
    if args[0] == 'push':
        queue.append(int(args[1]))
    elif args[0] == 'pop':
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)
    elif args[0] == 'size':
        result.append(len(queue))
    elif args[0] == 'empty':
        if queue:
            result.append(0)
        else:
            result.append(1)
    elif args[0] == 'front':
        if queue:
            result.append(queue[0])
        else:
            result.append(-1)
    elif args[0] == 'back':
        if queue:
            result.append(queue[-1])
        else:
            result.append(-1)

for i in range(N):
    menu = list(map(str, input().split()))
    queue_instruction(menu)

for r in result:
    print(r)
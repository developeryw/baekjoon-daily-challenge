import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

def queue_instruction(inst):
    menu = inst[0]

    if menu == 'push':
        queue.append(inst[1])
    elif menu == 'pop':
        if queue:
            num = queue.popleft()
            print(num)
        else:
            print(-1)
    elif menu == 'size':
        print(len(queue))
    elif menu == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif menu == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif menu == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

N = int(input())

for i in range(N):
    do = list(input().split())
    queue_instruction(do)
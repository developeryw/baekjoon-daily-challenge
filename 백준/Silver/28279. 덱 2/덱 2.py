import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deque = deque()

def de_instruction(n, inpt):
    if n == 1:
        deque.appendleft(inpt[1])
    elif n == 2:
        deque.append(inpt[1])
    elif n == 3:
        if deque:
            element= deque.popleft()
            print(element)
        else:
            print(-1)
    elif n == 4:
        if deque:
            element = deque.pop()
            print(element)
        else:
            print(-1)
    elif n == 5:
        print(len(deque))
    elif n == 6:
        if not deque:
            print(1)
        else:
            print(0)
    elif n == 7:
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif n == 8:
        if deque:
            print(deque[-1])
        else:
            print(-1)

for i in range(N):
    temp = list(map(int, input().split()))
    de_instruction(temp[0], temp)
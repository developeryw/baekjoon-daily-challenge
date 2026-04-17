import sys
input = sys.stdin.readline
from collections import deque

a, p = map(int, input().split())
stack = []
stack.append(a)

while True:
    a = list(map(int, str(a)))
    number = 0

    for i in a:
        number += i ** p

    if number in stack:
        idx = stack.index(number)
        del stack[idx:]

        print(len(stack))
        break
    else:
        stack.append(number)
        a = number
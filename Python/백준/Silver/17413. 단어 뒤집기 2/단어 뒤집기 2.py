import sys
input = sys.stdin.readline
from collections import deque

string = deque(map(str, input().rstrip()))

stack = []
result = ""

while string:
    cur = string.popleft()

    if cur == "<":
        if stack:
            for i in range(len(stack)):
                tmp = stack.pop()
                result += tmp
             
        while cur != ">":
            result += cur
            cur = string.popleft()

        result += cur
    elif cur == " ":
        for i in range(len(stack)):
            tmp = stack.pop()
            result += tmp
        result += cur
    else:
        stack.append(cur)

if stack:
     for i in range(len(stack)):
            tmp = stack.pop()
            result += tmp

print(result)
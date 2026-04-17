import sys
input = sys.stdin.readline
from collections import deque

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

n, kjm, lhs = map(int, input().split())

number = deque(i for i in range(1, n+1))
dq = deque()
round = 1


while True:
    if len(number) == 1:
        round += 1
        dq.append(number.pop())
        number = dq
        dq = deque()
        continue
    elif not number:
        round += 1
        number = dq
        dq = deque()
        continue

    a = number.popleft()
    b = number.popleft()

    if (a == kjm and b == lhs) or (a == lhs and b == kjm):
        print(round)
        break
    elif a == kjm or b == kjm:
        dq.append(kjm)
    elif a == lhs or b == lhs:
        dq.append(lhs)
    else:
        dq.append(a)

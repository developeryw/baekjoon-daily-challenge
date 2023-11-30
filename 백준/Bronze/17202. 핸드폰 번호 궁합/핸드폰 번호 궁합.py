import sys
input = sys.stdin.readline
from collections import deque

A = list(input().rstrip())
B = list(input().rstrip())
cal = deque()
compatibility = 0

for j in range(len(A)):
    cal.append(int(A[j]))
    cal.append(int(B[j]))

def calculate():
    for i in range(len(cal)-1):
        a = cal.popleft()
        b = cal[0]
        temp = (a + b) % 10

        cal.append(temp)

    cal.popleft()

while len(cal) > 2:
    calculate()

print(cal[0], cal[1], sep="")
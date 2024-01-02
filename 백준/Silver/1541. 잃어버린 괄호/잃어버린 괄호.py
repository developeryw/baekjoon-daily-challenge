import sys
input = sys.stdin.readline
from collections import deque

equation = list(input().rstrip())
equation.append(')')

number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
cur = len(equation) - 1
dq = deque(')')

while cur >= 0:
    if equation[cur] == '-':
        equation.insert(cur + 1, '(')
        dq.append('(')
        # equation.insert(cur, ')')
        # dq.append(')')
    elif equation[cur] in number and dq[-1] == '(':
        equation.insert(cur + 1, ')')
        dq.append(')')

    cur -= 1

if len(dq) % 2 != 0:
    equation.remove(')')

answer = 0
num = 0
exponent = 0

for i in range(len(equation) - 1, -1, -1):
    tmp = equation.pop()

    if tmp == ')':
        dq.popleft()
        exponent = 0
    elif tmp == '(':
        dq.popleft()
        exponent = 0
    elif tmp in number:
        num += int(tmp) * (10 ** exponent)
        exponent += 1
    elif tmp == '+':
        exponent = 0
    elif tmp == '-':
        answer -= num
        num = 0

print(answer + num)

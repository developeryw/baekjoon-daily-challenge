import sys
input = sys.stdin.readline

def isBalance(arr):
    stack = []

    for s in arr:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif s == ']' and stack and stack[-1] == '[':
            stack.pop()
        elif s == ')' or s == ']':
            return "no"

    if not stack:
        return "yes"
    else:
        return "no"

result = []

while True:
    line = input().rstrip()
    
    if line == '.':
        break

    check = isBalance(line)
    result.append(check)

for r in result:
    print(r)
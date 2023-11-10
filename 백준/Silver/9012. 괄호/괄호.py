import sys
input = sys.stdin.readline

def is_vps(arr):
    stack = []

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(1)
        elif arr[i] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

N = int(input())

for case in range(N):
    array = str(input().strip())
    isVPS = is_vps(array)
    print(isVPS)
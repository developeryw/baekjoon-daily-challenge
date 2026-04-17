import sys
input = sys.stdin.readline

N = int(input())
result = 0

for i in range(N):
    word = input().rstrip()
    stack = []

    for j in word:
        if not stack or stack[-1] != j:
            stack.append(j)
        elif stack[-1] == j:
            stack.pop()

    if not stack:
        result += 1

print(result)
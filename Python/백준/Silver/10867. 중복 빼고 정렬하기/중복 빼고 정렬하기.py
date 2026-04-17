import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
result = []

for i in num:
    if i not in result:
        result.append(i)

result.sort()

print(*result)
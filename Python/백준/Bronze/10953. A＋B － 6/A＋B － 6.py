import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    a, b = map(int, input().split(','))
    result.append(a+b)
    
print(*result, sep='\n')
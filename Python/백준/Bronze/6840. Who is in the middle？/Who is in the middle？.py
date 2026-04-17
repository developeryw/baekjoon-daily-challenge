import sys
input = sys.stdin.readline

result = []

for _ in range(3):
    tmp = int(input())
    result.append(tmp)
    
result.sort()

print(result[1])
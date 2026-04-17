import sys
input = sys.stdin.readline

result = 0

for _ in range(4):
    time = int(input())
    result += time
    
print(result // 60)
print(result % 60)
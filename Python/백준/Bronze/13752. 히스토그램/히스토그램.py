import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
    num = int(input())
    result.append(num)
    
for r in result:
    print("=" * r)
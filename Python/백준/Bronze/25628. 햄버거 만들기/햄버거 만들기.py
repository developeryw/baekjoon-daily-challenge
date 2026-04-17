import sys
input = sys.stdin.readline

a, b = map(int, input().split())
minimum = 0

if a // 2 > b:
    minimum = b
else:
    minimum = a // 2
    
print(minimum)
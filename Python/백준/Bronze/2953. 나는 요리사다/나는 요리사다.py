import sys
input = sys.stdin.readline

maximum = 0
result = 0

for i in range(1, 6):
    a, b, c, d = map(int, input().split())
    
    if maximum < a+b+c+d:
        maximum = a+b+c+d
        result = i
        
print(result, maximum)
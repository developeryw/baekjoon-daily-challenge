import sys
input = sys.stdin.readline

result = ""
maximum = 0

for _ in range(7):
    name, num = map(str, input().split())
    
    if int(num) > maximum:
        result = name
        maximum = int(num)
        
print(result)
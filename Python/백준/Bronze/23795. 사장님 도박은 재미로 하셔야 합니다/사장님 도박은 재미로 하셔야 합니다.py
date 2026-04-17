import sys
input = sys.stdin.readline

result = 0

while True:
    money = int(input())
    
    if money == -1:
        break
    else:
        result += money
        
print(result)
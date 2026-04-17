import sys
input = sys.stdin.readline

n = int(input())
menu = []

for _ in range(n):
    price = int(input())
    menu.append(price)
    
m = int(input())
result = 0

for _ in range(m):
    num = int(input())
    result += menu[num - 1]
    
print(result)
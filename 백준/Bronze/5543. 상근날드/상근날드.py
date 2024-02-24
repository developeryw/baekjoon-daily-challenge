import sys
input = sys.stdin.readline

price = []

for i in range(5):
    tmp = int(input())
    price.append(tmp)

result = min(price[0:3]) + min(price[3:5])

print(result - 50)
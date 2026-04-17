import sys
input = sys.stdin.readline

n = int(input())
total = 0
total2 = 0

for i in range(1, n+1):
    total += i
    total2 += (i ** 3)
    
print(total)
print(total ** 2)
print(total2)
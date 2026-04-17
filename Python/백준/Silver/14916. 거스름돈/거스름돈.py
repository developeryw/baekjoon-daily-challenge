import sys
input = sys.stdin.readline

n = int(input())

five_coin = n // 5
remainder = n % 5
total = 0

if n == 1 or n == 3:
    total = -1
elif remainder == 0:
    total = five_coin
elif remainder % 2 == 0:
    total = total + five_coin + (remainder // 2)
else:
    total = total + five_coin - 1 + (remainder + 5) // 2

print(total)
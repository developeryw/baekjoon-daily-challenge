import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

if (b - n) + n == a:
    print("Anything")
elif (b - n) + n < a:
    print("Subway")
else:
    print("Bus")
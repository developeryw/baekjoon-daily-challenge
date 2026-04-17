import sys
import math
input = sys.stdin.readline

n = int(input())
maximum = 0

for _ in range(n):
    a, b, c = map(int, input().split())

    if a == b and b == c:
        maximum = max(10000 + a * 1000, maximum)
    elif (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
        arr = sorted([a, b, c])
        maximum = max(1000 + arr[1] * 100, maximum)
    else:
        maximum = max(max(a, b, c) * 100, maximum)

print(maximum)
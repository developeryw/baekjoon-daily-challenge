import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = N-M

if result < 0:
    print(result * (-1))
else:
    print(result)
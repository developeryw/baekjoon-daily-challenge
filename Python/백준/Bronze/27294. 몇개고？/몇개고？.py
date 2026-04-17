import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if b == 0 and (a >= 12 and a <= 16):
    print(320)
else:
    print(280)
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a == 0:
    print(1)
else:
    defence = a - a * (b / 100)
    if defence >= 100:
        print(0)
    else:
        print(1)
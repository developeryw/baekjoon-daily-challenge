import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

if a % b == 0:
    print(a)
elif b % a == 0:
    print(b)
else:
    start = 2

    while True:
        if a * start % b == 0:
            print(a * start)
            break
        else:
            start += 1
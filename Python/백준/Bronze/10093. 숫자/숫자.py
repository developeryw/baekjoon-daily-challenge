import sys
input = sys.stdin.readline

start, last = map(int, input().split())
start, last = min(start, last), max(start, last)

if last - start > 0:
    print(last - start - 1)

    for i in range(start + 1, last):
        print(i, end=" ")
else:
    print(0)
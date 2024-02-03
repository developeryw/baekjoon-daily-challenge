import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
start = 0

while True:
    if (start % 15 + 1 == E) and (start % 28 + 1 == S) and (start % 19 + 1 == M):
        print(start + 1)
        break

    start += 1
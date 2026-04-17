import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

day = (V - B) // (A - B)
last = (V - B) % (A - B)

if last > 0:
    day += 1

print(day)
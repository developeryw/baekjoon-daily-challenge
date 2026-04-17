import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
wid = 0
length = 0

if w - x > x - 0:
    wid = x - 0
else:
    wid = w - x

if h - y > y - 0:
    length = y - 0
else:
    length = h - y

print(min(wid, length))
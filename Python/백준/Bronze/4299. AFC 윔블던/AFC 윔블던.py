import sys
input = sys.stdin.readline

s, d = map(int, input().split())

if (s+d) % 2 == 0 and s >= d:
    a = (s+d)//2
    print(a, s-a)
else:
    print(-1)
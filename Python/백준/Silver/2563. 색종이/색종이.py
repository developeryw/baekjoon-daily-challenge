import sys
input = sys.stdin.readline

white = [[0 for j in range(100)] for i in range(100)]
N = int(input())

for k in range(0, N, 1):
    x, y = map(int, input().split())
    for m in range(x, x+10, 1):
        for n in range(y, y+10, 1):
            white[m][n] = 1

wide = 0

for a in range(0, 100, 1):
    for b in range(0, 100, 1):
        if white[a][b] == 1:
            wide += 1

print(wide)
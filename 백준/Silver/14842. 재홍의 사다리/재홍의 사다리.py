import sys
input = sys.stdin.readline

W, H, N = map(int, input().split())
S = 0
section = H / N

if N % 2 == 0:
    start = 0
else:
    start = 1

for i in range(start, N, 2):
    S += (section * i)

S *= 2

print(round(S, 6))
import sys
input = sys.stdin.readline

N = int(input())
dots = 0
initial = 2

for i in range(1, N+1):
    initial = initial + 2 ** (i-1)

dots = initial ** 2
print(dots)
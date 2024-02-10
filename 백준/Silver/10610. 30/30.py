import sys
input = sys.stdin.readline

N = list(map(int, input().rstrip()))
total = sum(N)

if 0 not in N or total % 3 != 0:
    print(-1)
    exit(0)

N = sorted(N, reverse=True)

print(*N, sep="")

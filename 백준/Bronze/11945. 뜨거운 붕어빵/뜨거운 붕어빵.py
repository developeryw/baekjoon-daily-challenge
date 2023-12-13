import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pang = []

for i in range(N):
    temp = list(map(int, input().rstrip()))
    pang.append(temp)

for j in range(N):
    for k in range(M // 2):
        pang[j][k], pang[j][M-1-k] = pang[j][M-1-k], pang[j][k]

for r in pang:
    for s in r:
        print(s, end="")
    print()
    
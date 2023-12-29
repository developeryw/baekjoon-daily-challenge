import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = {}

for i in range(N):
    arr = input().rstrip()
    S[arr] = 0

for j in range(M):
    arr = input().rstrip()
    if arr in S:
        S[arr] += 1

cnt = 0

for k in S.values():
    if k > 0:
        cnt += k

print(cnt)

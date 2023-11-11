import sys
input = sys.stdin.readline

T = int(input())
result = []

for i in range(T):
    N, M = map(int, input().split())
    num = 1
    den = 1

    for j in range(M, M-N, -1):
        num *= j
    for k in range(1, N+1):
        den *=k

    result.append(int(num / den))

for r in result:
    print(r)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0
result = {}
printing = []

for i in range(N+M):
    temp = input()

    if temp in result:
        result[temp] += 1
    else:
        result[temp] = 1

for r in result:
    if result[r] > 1:
        cnt += 1
        printing.append(r)

print(cnt)
printing = sorted(printing)

for k in printing:
    print(k, end="")
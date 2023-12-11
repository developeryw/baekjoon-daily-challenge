import sys
input = sys.stdin.readline

N, M = map(int, input().split())
street = []
row = 0
col = 0
visited = 0

for i in range(N):
    temp = list(map(int, input().split()))
    street.append(temp)

for j in range(N):
    for k in range(M):
        if street[j][k] == 1:
            row += ((-1) ** visited) * (j+1)
            col += ((-1) ** visited) * (k+1)
            visited += 1

row = abs(row)
col = abs(col)

print(row+col)
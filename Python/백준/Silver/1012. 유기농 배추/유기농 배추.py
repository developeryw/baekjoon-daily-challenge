import sys
input = sys.stdin.readline
from collections import deque

r = [-1, 1, 0, 0] # 왼, 오, -, -
c = [0, 0, -1, 1] # -, -, 아래, 위

def bfs(x, y, matrix):
    matrix[x][y] = 0
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            tmp_x = x + r[k]
            tmp_y = y + c[k]
            
            if tmp_x < 0 or tmp_x >= M or tmp_y < 0 or tmp_y >= N: # 범위를 벗어날 경우
                continue

            if matrix[tmp_x][tmp_y] == 1:
                matrix[tmp_x][tmp_y] = 0
                queue.append((tmp_x, tmp_y))

    return matrix

T = int(input())
result = []

for _ in range(T):
    M, N, K = map(int, input().split())

    land = [[0] * (N) for _ in range(M)]
    cnt = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        land[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if land[i][j] == 1:
                land = bfs(i, j, land)
                cnt += 1

    result.append(cnt)

print(*result, sep="\n")
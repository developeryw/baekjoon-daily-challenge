import sys
input = sys.stdin.readline
from collections import deque

move_x = [-1, -1, -1, 0, 0, 1, 1, 1]
move_y = [-1, 0, 1, -1, 1, -1, 0, 1]

def count_island(x, y, matrix):
    matrix[x][y] = 0
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for k in range(8):
            tmp_x = x + move_x[k]
            tmp_y = y + move_y[k]

            if tmp_x < 0 or tmp_x >= h or tmp_y < 0 or tmp_y >= w:
                continue

            if matrix[tmp_x][tmp_y] == 1:
                matrix[tmp_x][tmp_y] = 0
                queue.append((tmp_x, tmp_y))

    return matrix

result = []

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    world = []
    cnt = 0

    for _ in range(h):
        tmp = list(map(int, input().split()))
        world.append(tmp)

    for i in range(h):
        for j in range(w):
            if world[i][j] == 1:
                world = count_island(i, j, world)
                cnt += 1

    result.append(cnt)

print(*result, sep="\n")
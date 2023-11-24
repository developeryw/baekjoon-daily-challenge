import sys
input = sys.stdin.readline

N = int(input())
friends = []
maximum = 0

def bfs(graph, idx):
    cnt = 0
    visited = [0] * N

    for k in range(N):
        if k == idx:
            continue

        if graph[idx][k] == 'Y':
            cnt += 1
        else:
            for m in range(N):
                if graph[idx][m] == 'Y' and graph[k][m] == 'Y':
                    cnt += 1
                    break

    return cnt

for i in range(N):
    isFriend = list(input().rstrip())
    friends.append(isFriend)

for j in range(N):
    temp = bfs(friends, j)
    maximum = max(maximum, temp)

print(maximum)
import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = {key: [] for key in range(1, N+1)}

for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


for k in graph:
    graph[k].sort()

visited1 = [0] * (N+1)
def dfs(v):
    print(v, end=" ")
    visited1[v] = 1

    for j in graph[v]:
        if visited1[j] == 0:
            dfs(j)

visited2 = [0] * (N+1)
def bfs(v):
    queue = deque([v])
    visited2[v] = 1

    while True:
        v = queue.popleft()
        print(v, end=" ")

        for j in graph[v]:
            if visited2[j] == 0:
                queue.append(j)
                visited2[j] = 1

        if not queue:
            break
            
dfs(V)
print()
bfs(V)
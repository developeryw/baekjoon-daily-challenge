import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
connected = {key: [] for key in range(1, N+1)}

def bfs(graph):
   node = 1
   visit = deque([1])
   visited = [0] * (N+1)
   visited[1] = 1
   counting = 1

   while True:
       while visit:
           cur = visit.popleft()
           for j in graph[cur]:
               if visited[j] == 0:
                   visit.append(j)
                   visited[j] = 1

       node += 1

       if node > N:
           break

       if visited[node] == 0:
           visit.append(node)
           visited[node] = 1
           counting += 1

   return counting

for i in range(M):
    n1, n2 = map(int, input().split())
    connected[n1].append(n2)
    connected[n2].append(n1)

result = bfs(connected)

print(result)
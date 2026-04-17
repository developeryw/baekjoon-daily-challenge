import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []
result = []

for i in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        if heap:
            minimum = heapq.heappop(heap)
            result.append(minimum)
        else:
            result.append(0)

print(*result, sep="\n")
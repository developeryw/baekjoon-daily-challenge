import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
left = list(map(int, input().split()))
left_people = {}
ordered = []

for i in range(1, N+1):
    left_people[i] = left[i-1]

for j in range(N, 0, -1):
    cur = 0
    isDone = left_people[j]

    while isDone:
        if ordered[cur] > j:
            cur += 1
            isDone -= 1

    ordered.insert(cur, j)

for r in ordered:
    print(r, end=" ")
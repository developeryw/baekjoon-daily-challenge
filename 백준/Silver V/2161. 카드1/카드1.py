import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
cards = deque([num for num in range(1, N+1)])
result = []

while len(result) < N:
    if cards:
        card = cards.popleft()
        result.append(card)

    if cards:
        card = cards.popleft()
        cards.append(card)

print(*result)
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
card_pack = deque(map(int, input().split()))
card_pack.appendleft(0)

for i in range(1, N+1):
    for j in range(1, i // 2 + 1):
        if card_pack[i] < card_pack[i-j] + card_pack[j]:
            card_pack[i] = card_pack[i-j] + card_pack[j]

print(card_pack[N])
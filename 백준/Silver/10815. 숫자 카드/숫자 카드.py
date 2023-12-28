import sys
input = sys.stdin.readline

N = int(input())
SG_cards = list(map(int, input().split()))

M = int(input())
temp = list(map(int, input().split()))
comp_cards = {x: 0 for x in temp}

for n in SG_cards:
    if n in comp_cards:
        comp_cards[n] += 1

for r in comp_cards.values():
    print(r, end=" ")
import sys
input = sys.stdin.readline

N = int(input())
cards = {}

for i in range(N):
    number = int(input())
    if number in cards:
        cards[number] += 1
    else:
        cards[number] = 1

result = sorted(cards.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])
import sys
input = sys.stdin.readline

N = int(input())
game = []
result = 0

for i in range(N):
    level = int(input())
    game.append(level)

for j in range(N-1, 0, -1):
    if game[j] <= game[j-1]:
        descend = game[j-1] - game[j] + 1
        game[j-1] -= descend
        result += descend

print(result)
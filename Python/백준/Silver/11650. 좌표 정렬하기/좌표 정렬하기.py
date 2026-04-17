import sys
input = sys.stdin.readline

N = int(input())
coordinate = []

for i in range(N):
    coordinate.append(list(map(int, input().split())))

coordinate.sort(key=lambda x: (x[0], x[1]))

for c, d in coordinate:
    print(c, d)
import sys
input = sys.stdin.readline

N = int(input())
P = sorted(list(map(int, input().split())))
shortest = 0

for i in range(1, len(P)):
    P[i] += P[i-1]
    shortest += P[i]

print(shortest + P[0])
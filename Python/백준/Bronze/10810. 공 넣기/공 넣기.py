import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0] * 101

for x in range(1, M+1, 1):
    i, j, k = map(int, input().split())
    for y in range(i-1, j, 1):
        basket[y+1] = k

for z in range(1, N+1, 1):
    print(basket[z], end=" ")

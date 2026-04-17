import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0] * (N+1)

tmp1 = 0
tmp2 = 0

for x in range(0, N+1, 1):
    basket[x] = x

for y in range(0, M, 1):
    i, j = map(int, input().split())
    tmp1 = basket[i]
    tmp2 = basket[j]
    basket[i] = tmp2
    basket[j] = tmp1

for z in range(1, N+1, 1):
    print(basket[z], end=" ")

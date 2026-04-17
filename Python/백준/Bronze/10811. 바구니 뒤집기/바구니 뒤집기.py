import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0] * 101
temp = 0

for n in range(1, N+1, 1):
    basket[n] = n

for x in range(M):
    i, j = map(int, input().split())
    k = (j-i)//2
    for y in range(0, k+1, 1):
        temp = basket[j-y]
        basket[j-y] = basket[i+y]
        basket[i+y] = temp

for z in range(1, N+1, 1):
    print(basket[z], end=" ")

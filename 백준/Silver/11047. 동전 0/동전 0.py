import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
money = []

for i in range(N):
    cash = int(input())
    money.append(cash)

money = sorted(money, reverse=True)
idx = 0

while K > 0:
    if K >= money[idx]:
        coins = K // money[idx]
        cnt += coins
        K -= coins * money[idx]
    else:
        idx += 1

print(cnt)
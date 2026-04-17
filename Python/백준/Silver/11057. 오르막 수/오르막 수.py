import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1

for j in range(2, N+1):
    for k in range(9, -1, -1):
        if  k == 9:
            dp[j][k] = dp[j-1][k]
        else:
            dp[j][k] = sum(dp[j-1][k:])

print(sum(dp[N]) % 10007)
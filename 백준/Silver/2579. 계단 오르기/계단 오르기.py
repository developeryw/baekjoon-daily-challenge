import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] * 301

for i in range(1, N+1):
    stairs[i] = int(input().rstrip())

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for j in range(4, N+1):
    dp[j] = max(dp[j-2] + stairs[j], dp[j-3] + stairs[j-1] + stairs[j])

print(dp[N])
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
dp = [-1000 for _ in range(n+1)]
dp[0] = num[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + num[i], num[i])

print(max(dp))
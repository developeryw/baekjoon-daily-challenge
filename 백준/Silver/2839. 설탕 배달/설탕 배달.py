import sys
input = sys.stdin.readline

N = int(input())
dp = [5001 for _ in range(N+1)]
start = 1

for i in range(3, N+1, 3):
    dp[i] = start
    start += 1

start = 1
for j in range(5, N+1, 5):
    dp[j] = start
    start += 1

for k in range(3, N+1):
    dp[k] = min(dp[k-3] + 1, dp[k-5] + 1, dp[k])

if dp[N] > 5000:
    print(-1)
else:
    print(dp[N])
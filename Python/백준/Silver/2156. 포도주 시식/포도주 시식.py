import sys
input = sys.stdin.readline


n = int(input())
wine = []

for i in range(n):
    tmp = int(input())
    wine.append(tmp)

if n == 1 or n == 2:
    print(sum(wine))
else:
    dp = [0] * n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(dp[0] + wine[2], dp[1], wine[1] + wine[2])

    for j in range(3, n):
        dp[j] = max(dp[j-2] + wine[j], dp[j-1], dp[j-3] + wine[j-1] + wine[j])

    print(dp[n-1])
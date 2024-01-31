import sys
input = sys.stdin.readline

T = int(input())
num = []
result = []

for i in range(T):
    n = int(input())
    num.append(n)

maximum = max(num)

dp = [0] * (maximum + 4)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for j in range(4, maximum + 1):
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

for k in num:
    print(dp[k])
import sys
input = sys.stdin.readline

S = list(map(int, input().rstrip()))
cur = S[0]
cnt0 = 0
cnt1 = 0

for i in S:
    if i != cur and i == 1:
        cur = i
        cnt1 += 1
    elif i != cur and i == 0:
        cur = i
        cnt0 += 1

print(max(cnt0, cnt1))

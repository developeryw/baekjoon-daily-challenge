import sys
input = sys.stdin.readline

X = int(input())
num = 1 # 분자
den = 1 # 분모

isStart = 0
ans = 1
diff = 1
cnt = 1

while True:
    if X == ans:
        isStart = 1
        break
    elif X < ans:
        break

    ans += diff
    diff += 1
    cnt += 1

isOdd = 1

if isStart == 1:
    if cnt % 2 == 0:
        isOdd = 0

    if isOdd == 0:
        num = 1
        den = cnt
    else:
        num = cnt
        den = 1
else:
    cnt -= 1
    ans -= cnt

    if cnt % 2 == 0:
        isOdd = 0

    if isOdd == 0:
        num = 1 + (X - ans)
        den = cnt - (X - ans)
    else:
        num = cnt - (X - ans)
        den = 1 + (X - ans)

print("%d/%d" % (num, den))
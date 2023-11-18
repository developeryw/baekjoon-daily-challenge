import sys
input = sys.stdin.readline

N = str(input().rstrip())
num = [0] * 10

for i in range(len(N)):
    idx = int(N[i])
    num[idx] += 1

if (num[6] + num[9]) % 2 == 0:
    num[6] = num[9] = (num[6] + num[9]) / 2
else:
    num[6] = num[9] = (num[6] + num[9]) // 2 + 1

set_cnt = max(num)
idx = num.index(set_cnt)

print(int(set_cnt))
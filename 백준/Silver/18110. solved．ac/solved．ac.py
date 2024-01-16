import sys
input = sys.stdin.readline

n = int(input())
levels = []

if n == 0:
    print('0')
    exit(0)

def rounding(num):
    if num - int(num) == 0.5:
        return int(num) + 1
    else:
        return round(num)

for i in range(n):
    tmp = int(input())
    levels.append(tmp)

levels.sort(reverse=True)

cut = rounding(n * 0.15)

total = 0
for j in range(cut, n - cut):
    total += levels[j]

print(rounding(total / (n - cut * 2)))
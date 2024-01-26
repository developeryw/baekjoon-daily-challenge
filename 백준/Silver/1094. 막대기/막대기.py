import sys
input = sys.stdin.readline

X = int(input())
stick = 64
total = 64
cnt = 1

while total > X:
    stick /= 2

    if total - stick >= X:
        total -= stick
    else:
        cnt += 1

print(cnt)
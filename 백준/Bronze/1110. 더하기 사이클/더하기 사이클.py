import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
num = N

while True:
    left = num // 10
    right = num % 10

    num = (left + right) % 10 + right * 10

    cnt += 1

    if num == N:
        print(cnt)
        break
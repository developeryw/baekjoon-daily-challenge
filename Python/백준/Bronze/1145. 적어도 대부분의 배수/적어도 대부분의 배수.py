import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
input()

result = min(num)

while True:
    cnt = 0

    for n in num:
        if result % n == 0:
            cnt += 1

    if cnt >= 3:
        print(result)
        break

    result += 1

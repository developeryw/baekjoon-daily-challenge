import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
answer = [1, 2, 3, 4, 5]
input()

while True:
    if num == answer:
        break

    for i in range(0, len(num)-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
            print(*num, sep=" ")
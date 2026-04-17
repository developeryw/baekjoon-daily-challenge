import sys
input = sys.stdin.readline

N = int(input())
num = 0

for _ in range(N):
    num += int(input())

if num >= (N // 2) + 1:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
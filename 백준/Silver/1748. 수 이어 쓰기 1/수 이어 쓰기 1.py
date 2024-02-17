import sys
input = sys.stdin.readline

N = input().rstrip()
num = 0

for i in range(1, len(N)):
    num += 9 * (10 ** (i - 1)) * i

num += len(N) * (int(N) - 10 ** (len(N) - 1) + 1)

print(num)
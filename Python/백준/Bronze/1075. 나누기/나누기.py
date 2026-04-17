import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

start = n // 100 * 100
minimum = n + 99

for num in range(start, start + 100):
    if num % f == 0:
        minimum = min(num, minimum)

print("%02d" % (minimum % 100))
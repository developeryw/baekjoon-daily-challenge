import sys
input = sys.stdin.readline

S = int(input())
start = 1
cnt = 0

while S >= 0:
    S -= start
    cnt += 1
    start += 1

print(cnt - 1)
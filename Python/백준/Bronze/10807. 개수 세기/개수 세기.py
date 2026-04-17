import sys
input = sys.stdin.readline

N = int(input())
numarr = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(0, N, 1):
    if (numarr[i] == v):
        cnt += 1

print(cnt)
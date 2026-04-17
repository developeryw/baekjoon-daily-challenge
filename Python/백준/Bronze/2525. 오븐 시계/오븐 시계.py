import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

addh = C//60
addm = C%60

resulth = A+addh
resultm = B+addm

if (resultm)//60 >= 1:
    up = 1
else:
    up = 0

print((resulth+up)%24, resultm%60)
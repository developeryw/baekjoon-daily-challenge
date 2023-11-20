import sys
input = sys.stdin.readline

N = int(input())
inpt = []

for i in range(1, N+1):
    temp = input().rstrip()
    inpt.append(str(i) + '. ' + temp)

for r in inpt:
    print(r)
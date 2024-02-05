import sys
input = sys.stdin.readline

L = int(input())
arr = list(map(str, input().rstrip()))

total = 0
r = 31
M = 1234567891

for i in range(L):
    total += (ord(arr[i]) - 96) * (r ** i)

print(total % M)

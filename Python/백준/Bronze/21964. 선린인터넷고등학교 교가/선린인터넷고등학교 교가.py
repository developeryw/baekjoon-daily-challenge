import sys
input = sys.stdin.readline

n = int(input())
arr = input().rstrip()

length = len(arr) - 5

for i in range(length, n):
    print(arr[i], end="")
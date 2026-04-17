import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    l, arr = map(str, input().split())

    l = int(l)
    arr = list(arr)

    arr.pop(l-1)

    print(*arr, sep="")
    
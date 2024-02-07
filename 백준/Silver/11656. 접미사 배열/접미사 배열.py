import sys
input = sys.stdin.readline

S = list(map(str, input().rstrip()))
arr = [""] * (len(S))

for i in range(len(S)):
    for j in range(i, len(S)):
        arr[i] += S[j]

arr.sort()

print(*arr, sep="\n")
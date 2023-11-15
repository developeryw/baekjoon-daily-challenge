import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[0 for x in range(M)] for y in range(N)]
B = [[0 for a in range(M)] for b in range(N)]

for i in range(0, N, 1):
    line = list(map(int, input().split()))
    A[i] = line

for j in range(0, N, 1):
    line = list(map(int, input().split()))
    B[j] = line

for n in range(0, N, 1):
    for m in range(0, M, 1):
        print(A[n][m] + B[n][m], end=" ")
    print("")
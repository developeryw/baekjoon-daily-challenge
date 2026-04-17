import sys
input = sys.stdin.readline

N, X = map(int, input().split())
numarr = list(map(int, input().split()))

for i in range(0, N, 1):
    if numarr[i] < X:
        print(numarr[i], end=" ")
import sys
input = sys.stdin.readline

T = int(input())

for i in range(0, T, 1):
    R, S = input().split()

    for j in range(len(S)):
        for k in range(0, int(R), 1):
            print(S[j], end="")

    print("")
import sys
input = sys.stdin.readline

N = int(input())

for k in range(N):
    for i in range(2):
        for j in range(1, N+1):
            if (i + j) % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
        print("")
import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1, 1):
    for j in range(1, i+1, 1):
        print("*", end="")
    print("")
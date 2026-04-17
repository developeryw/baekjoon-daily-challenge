import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print("")
    exit(0)

divisor = 2

while divisor <= N:
    if N % divisor == 0:
        print(divisor)
        N = N // divisor
    else:
        divisor += 1
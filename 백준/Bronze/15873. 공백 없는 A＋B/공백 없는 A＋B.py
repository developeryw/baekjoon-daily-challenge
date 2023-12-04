import sys
input = sys.stdin.readline

N = int(input())

if N // 10 > 0 and N % 10 == 0:
    A = N // 100
    B = N % 100
else:
    A = N // 10
    B = N % 10

print(A+B)
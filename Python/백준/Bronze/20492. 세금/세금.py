import sys
input = sys.stdin.readline

N = int(input())

A = int(N - N * 0.22)
B = int(N - N * 0.2 * 0.22)

print(A, B)
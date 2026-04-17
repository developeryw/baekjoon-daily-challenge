import sys
input = sys.stdin.readline

n = int(input())
input()

for i in range(1, n+1):
    print(" " * (n - i), end="")
    print("*" * i)

for j in range(1, n):
    print(" " * j, end="")
    print("*" * (n - j))
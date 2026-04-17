import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    print("*" * i, end="")
    print(" " * (n - i), end="")
    print(" " * (n - i), end="")
    print("*" * i)

for j in range(1, n):
    print("*" * (n - j), end="")
    print(" " * j, end="")
    print(" " * j, end="")
    print("*" * (n - j))
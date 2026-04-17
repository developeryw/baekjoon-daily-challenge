import sys
input = sys.stdin.readline

T = int(input())

for i in range(0, T, 1):
    str = input()

    print(str[0], end="")
    print(str[-2])
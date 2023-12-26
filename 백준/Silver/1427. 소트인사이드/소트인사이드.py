import sys
input = sys.stdin.readline

number = list(map(int, input().rstrip()))
number.sort(reverse=True)

for n in number:
    print(n, end="")
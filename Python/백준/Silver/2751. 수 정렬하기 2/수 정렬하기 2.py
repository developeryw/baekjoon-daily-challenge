import sys
input = sys.stdin.readline

number = set()

N = int(input())

for i in range(N):
    n = int(input())
    number.add(n)

number = sorted(number)

for r in number:
    print(r)
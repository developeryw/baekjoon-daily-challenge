import sys
input = sys.stdin.readline

people = list(map(int, input().split()))
x, y, r = map(int, input().split())

if x in people:
    idx = people.index(x)
    print(idx + 1)
else:
    print(0)
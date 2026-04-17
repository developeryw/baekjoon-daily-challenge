import sys
input = sys.stdin.readline

n, l = map(int, input().split())
fruits = sorted(list(map(int, input().split())))
input()

for fruit in fruits:
    if fruit > l:
        print(l)
        exit(0)
    else:
        l += 1

print(l)

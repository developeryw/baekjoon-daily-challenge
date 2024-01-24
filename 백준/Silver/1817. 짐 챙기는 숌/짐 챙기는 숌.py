import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))

if N == 0:
    print(0)
    exit(0)

boxes = 0
cur = M

for i in range(N):
    if cur < books[i]:
        boxes += 1
        cur = M
        cur -= books[i]
    else:
        cur -= books[i]

if cur != M:
    boxes += 1

print(boxes)
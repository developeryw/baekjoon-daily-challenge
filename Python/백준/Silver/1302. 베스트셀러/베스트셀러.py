import sys
input = sys.stdin.readline

N = int(input())
books = {}

for i in range(N):
    title = input().rstrip()
    if title in books:
        books[title] += 1
    else:
        books[title] = 0

books = sorted(books.items(), key= lambda x: (-x[1], x[0]))

print(books[0][0])
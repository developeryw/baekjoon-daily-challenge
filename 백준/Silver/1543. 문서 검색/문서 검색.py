import sys
input = sys.stdin.readline

doc = input().rstrip()
find = input().rstrip()

cur = 0
length = len(find)
result = 0

while cur <= len(doc) - length + 1:
    if doc[cur:cur+length] == find:
        result += 1
        cur += length
    else:
        cur += 1

print(result)
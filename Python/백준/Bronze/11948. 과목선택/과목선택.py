import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = int(input())
f = int(input())

result = a + b + c + d - min(a, b, c, d)
result += max(e, f)

print(result)
import sys
input = sys.stdin.readline

X, Y = map(str, input().split())

x = int(X[::-1])
y = int(Y[::-1])

result = int(str(x+y)[::-1])

print(result)

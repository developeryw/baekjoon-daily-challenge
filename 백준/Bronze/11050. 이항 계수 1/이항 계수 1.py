import sys
input = sys.stdin.readline

def factorial(num):
    if num <= 1:
        return 1

    return num * factorial(num - 1)

N, K = map(int, input().split())
a = factorial(N)
b = factorial(N-K)
c = factorial(K)

result = int(a / (b * c))

print(result)
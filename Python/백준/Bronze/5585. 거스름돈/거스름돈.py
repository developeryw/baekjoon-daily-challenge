import sys
input = sys.stdin.readline

N = int(input())
N = 1000 - N

cash =  (500, 100, 50, 10, 5, 1)
result = 0

for i in cash:
    result += (N // i)
    N -= (N // i) * i

print(result)

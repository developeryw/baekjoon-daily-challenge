import sys
input = sys.stdin.readline

N = int(input())
exp = 1
cnt = 0

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

fact = factorial(N)

while True:
    if fact % (10 ** exp) == 0:
        cnt += 1
        exp += 1
    else:
        break

print(cnt)
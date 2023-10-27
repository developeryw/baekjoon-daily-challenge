import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def isPrime(x):
    if x == 1:
        return 0
    
    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            return 0
    return 1

for j in range(M, N+1):
    if isPrime(j) == 1:
        print(j)
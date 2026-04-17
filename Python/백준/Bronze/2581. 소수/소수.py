import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
prime = list()
sum_prime = 0

for i in range(M, N+1):
    isPrime = 0

    for j in range(1, i+1):
        if i % j == 0:
            isPrime += 1
    if isPrime == 2:
        prime.append(i)
        sum_prime += i

if len(prime) == 0:
    print(-1)
else:
    print(sum_prime)
    print(prime[0])
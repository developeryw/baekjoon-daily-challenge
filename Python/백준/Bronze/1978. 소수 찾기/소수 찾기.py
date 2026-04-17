import sys
input = sys.stdin.readline

N = int(input())
prime = list(map(int, input().split()))
cnt_prime = 0

for i in range(N):
    cnt_divisor = 0
    
    for j in range(1, prime[i] + 1):
        if prime[i] % j == 0:
            cnt_divisor += 1
        j += 1

    if cnt_divisor == 2:
        cnt_prime += 1

print(cnt_prime)
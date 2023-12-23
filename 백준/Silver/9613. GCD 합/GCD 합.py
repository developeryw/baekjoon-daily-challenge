import sys
input = sys.stdin.readline

T = int(input())
result = []

def gcd(num1, num2):
    answer = 1
    prime = 2

    while True:
        if prime > num1 and prime > num2:
            break
            
        if num1 % prime == 0 and num2 % prime == 0:
            answer *= prime
            num1 //= prime
            num2 //= prime
        else:
            prime += 1

    return answer

def every_test_cases(arr):
    total = 0

    for i in range(1, len(arr)-1):
        for j in range(i+1, len(arr)):
            total += gcd(arr[i], arr[j])

    return total

for k in range(T):
    N = list(map(int, input().split()))
    temp = every_test_cases(N)
    result.append(temp)

for r in result:
    print(r)
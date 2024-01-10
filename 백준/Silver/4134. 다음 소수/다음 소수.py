import sys
input = sys.stdin.readline

T = int(input())
result = []

def isprime(n):
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False

    return True

for i in range(T):
    number = int(input())
    while True:
        if number == 0 or number == 1:
            number = 2
            break

        if isprime(number):
            break

        number += 1

    result.append(number)

print(*result, sep="\n")
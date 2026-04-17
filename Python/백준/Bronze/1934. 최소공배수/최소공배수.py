import sys
input = sys.stdin.readline

N = int(input())

def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2

    return n1

def LCM(n1, n2):
    return (n1 * n2) // gcd(n1, n2)

result = []

for i in range(N):
    num1, num2 = map(int, input().split())
    lcm_i = LCM(num1, num2)
    result.append(lcm_i)

for r in result:
    print(r)
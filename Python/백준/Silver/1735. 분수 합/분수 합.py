import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a * d + c * b
denominator = b * d

mod = numerator % denominator
div = denominator

while mod > 0:
    tmp = mod
    mod = div % mod
    div = tmp

print(numerator // div, denominator // div)
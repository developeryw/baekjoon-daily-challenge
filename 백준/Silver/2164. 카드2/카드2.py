import sys
input = sys.stdin.readline

N = int(input())
original = N

if N == 1 or N == 2:
    print(N)
    exit(0)

exponent = 0
remainder = 0

while N // 2 != 0:
    if N >= 2:
        exponent += 1
        remainder += N % 2
        N = N // 2

if remainder == 0:
    print(original)
else:
    print(2 * (original - 2 ** exponent))
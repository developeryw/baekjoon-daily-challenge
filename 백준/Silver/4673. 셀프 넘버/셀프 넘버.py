import sys
input = sys.stdin.readline

number = [i+1 for i in range(10000)]

def generator(n):
    exponent = 1
    gen = n

    while n > 0:
        gen += n % (10 ** exponent)
        n //= (10 ** exponent)

    return gen

for i in range(1, 10001):
    num = generator(i)
    if num in number:
        number.remove(num)

print(*number, sep="\n")
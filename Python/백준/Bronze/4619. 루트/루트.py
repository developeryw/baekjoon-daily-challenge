import sys
input = sys.stdin.readline

while True:
    b, n = map(int, input().split())

    if b == 0 & n == 0:
        break

    end = int(b ** (1/n) + 2)
    dif = 1000000
    result = 0

    for i in range(1, end):
        if abs(b - i ** n) < dif:
            dif = abs(b - i ** n)
            result = i

    print(result)

import sys
input = sys.stdin.readline

N = int(input())
current = 1

while True:
    total = 0
    cur = current
    length = len(str(cur))

    total += cur
    for i in range(length):
        total += ((cur % (10 ** (i+1))) // (10 ** i))
        cur -= (cur % (10 ** (i+1)))

    if total == N:
        print(current)
        break
    elif current > N:
        print(0)
        break
    else:
        current += 1
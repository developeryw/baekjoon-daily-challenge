import sys
input = sys.stdin.readline

result = []

def prime(n):
    arr = [1] * (n+1)
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] == 1:
            for j in range(2 * i, n + 1, i):
                arr[j] = 0

    return arr

while True:
    num = int(input())

    if num == 0:
        break
    else:
        numbers = prime(2 * num)

        tmp = sum(numbers[num+1:2*num + 1])
        result.append(tmp)

print(*result, sep="\n")
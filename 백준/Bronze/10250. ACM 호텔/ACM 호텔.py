import sys
input = sys.stdin.readline

T = int(input())
result = []

def hotel(h, w, n):
    row, col = 0, 0

    for x in range(1, w+1):
        for y in range(1, h+1):
            if n == 0:
                break

            row = x
            col = y

            n -= 1

    return col * 100 + row

for i in range(T):
    H, W, N = map(int, input().split())
    answer = hotel(H, W, N)
    result.append(answer)

print(*result, sep="\n")
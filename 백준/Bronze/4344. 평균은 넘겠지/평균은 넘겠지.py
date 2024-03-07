import sys
input = sys.stdin.readline

C = int(input())
result = []

for i in range(C):
    N = list(map(int, input().split()))

    total = sum(N[1:len(N)])
    avg = total / N[0]

    total2 = 0

    for j in range(1, len(N)):
        if N[j] > avg:
            total2 += 1

    answer = (total2 / N[0]) * 100
    result.append(answer)

for r in result:
    print("{:.3f}".format(r) + "%")
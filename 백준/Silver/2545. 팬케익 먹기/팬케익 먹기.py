import sys
input = sys.stdin.readline

T = int(input())
result = []

for i in range(T):
    input()
    A, B, C, D = map(int, input().split())

    cake_size = A * B * C
    cake = [A, B, C]

    for j in range(D):
        cake.sort()
        
        if cake[0] > 0:
            cut1 = cake[0]
            if cake[1] > 0:
                cut2 = cake[1]
                cake[2] -= 1
            else:
                cut2 = cake[2]
                cake[1] -= 1
        else:
            cut1 = cake[1]
            cut2 = cake[2]

            cake[0] -= 1

        cake_size -= cut1 * cut2

    result.append(cake_size)

for r in result:
    print(r)

import sys
input = sys.stdin.readline

number = [0, 0, 0]
result = []

while True:
    W, D, H = map(int, input().split())

    if W == 0 and D == 0 and H == 0:
        break

    number[0] = W
    number[1] = D
    number[2] = H
    number = sorted(number)

    if (number[0] ** 2 + number[1] ** 2) == (number[2] ** 2):
        result.append("right")
    else:
        result.append("wrong")

for r in result:
    print(r)
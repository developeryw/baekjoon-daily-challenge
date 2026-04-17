import sys
input = sys.stdin.readline

result = []

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    if A % B == 0:
        result.append("multiple")
    elif B % A == 0:
        result.append("factor")
    else:
        result.append("neither")


for i in range(len(result) - 1):
    print(result[i])

print(result[len(result) - 1], end="")
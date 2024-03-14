import sys
input = sys.stdin.readline

result = []

while True:
    num1, num2 = map(int, input().split())

    if num1 == 0 and num2 == 0:
        break

    if num1 > num2:
        result.append("Yes")
    else:
        result.append("No")

print(*result, sep="\n")
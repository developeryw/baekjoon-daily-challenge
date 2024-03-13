import sys
input = sys.stdin.readline

result = 0

for i in range(10):
    num = int(input())

    if abs(100 - (result + num)) <= abs(100 - result):
        result += num
    else:
        break

print(result)
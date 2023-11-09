import sys
input = sys.stdin.readline

computers = {}
N = int(input().rstrip())
pair = int(input().rstrip())

for i in range(pair):
    num1, num2 = map(int, input().strip().split())

    if num1 not in computers:
        computers[num1] = []

    if num2 not in computers:
        computers[num2] = []

    computers[num1].append(num2)
    computers[num2].append(num1)

stack = [1]
current = 1
cnt = 0
isVisited = [0] * N

while stack:
    current = stack.pop()

    if isVisited[current - 1] == 0:
        isVisited[current - 1] = 1

        if current in computers:
            for number in computers[current]:
                stack.append(number)

for k in isVisited:
    if k > 0:
        cnt += 1

print(cnt - 1)
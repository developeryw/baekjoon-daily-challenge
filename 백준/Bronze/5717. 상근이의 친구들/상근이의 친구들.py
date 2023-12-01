import sys
input = sys.stdin.readline

result = []

while True:
    M, F = map(int, input().split())

    if M == 0 and F == 0:
        break

    result.append(M + F)

for r in result:
    print(r)
import sys
input = sys.stdin.readline

T = int(input())
result = []

for i in range(T):
    sentence = list(map(str, input().split()))
    result.append(sentence)

for r in result:
    for j in r:
        print(j[::-1], end=" ")
    print()
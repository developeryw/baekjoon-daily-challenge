import sys
input = sys.stdin.readline

result = []

while True:
    T = list(map(int, input().rstrip()))
    isTrue = True

    if len(T) == 1 and T[0] == 0:
        break

    for i in range(0, len(T) // 2):
        if T[i] != T[len(T) - i - 1]:
            isTrue = False

    result.append(isTrue)

for r in result:
    if r:
        print("yes")
    else:
        print("no")
import sys
input = sys.stdin.readline

N = int(input())
factorial = [0] * 21
factorial[0] = 1

for i in range(1, 20):
    factorial[i] = i * factorial[i-1]

if N == 0:
    print("NO")
else:
    for i in range(20, -1, -1):
        if N >= factorial[i]:
            N -= factorial[i]

    if N == 0:
        print("YES")
    else:
        print("NO")
        
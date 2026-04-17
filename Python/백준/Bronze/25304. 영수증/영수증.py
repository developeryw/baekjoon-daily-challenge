X = int(input())
N = int(input())
com = 0

for i in range(0, N, 1):
    a, b = map(int, input().split())
    com += a*b

if (X==com):
    print("Yes")
else:
    print("No")
import sys
input = sys.stdin.readline

T = int(input())
result = []

for i in range(T):
    N = int(input())
    closet = {}
    total = 1

    for j in range(N):
       cloth, kind = input().split()

       if kind in closet:
           closet[kind] += 1
       else:
           closet[kind] = 1

    for k in closet:
        total *= (closet[k] + 1)

    result.append(total - 1)

for r in result:
    print(r)

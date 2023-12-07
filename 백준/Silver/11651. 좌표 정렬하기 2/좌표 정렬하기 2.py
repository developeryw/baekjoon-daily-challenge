import sys
input = sys.stdin.readline

N = int(input())
coordinate = []

for i in range(N):
    temp = list(map(int, input().split()))
    coordinate.append(temp)

coordinate.sort(key= lambda x: (x[1], x[0]))

for c in coordinate:
    for num in c:
        print(num, end=" ")
    print()
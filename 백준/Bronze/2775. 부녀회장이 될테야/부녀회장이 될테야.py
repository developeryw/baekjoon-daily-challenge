import sys
input = sys.stdin.readline

T = int(input())
result = []

def apartment(K, N):
    apart = [num for num in range(N+1)]

    for x in range(K):
        for y in range(1, N+1):
            apart[y] += apart[y-1]

    return apart[N]

for i in range(T):
    k = int(input())
    n = int(input())

    people = apartment(k, n)
    result.append(people)

for r in result:
    print(r)
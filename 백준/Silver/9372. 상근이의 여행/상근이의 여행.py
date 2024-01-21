import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
result = []

def dfs(country, flight, cur):
    if not country[cur]:
        return 0

    country[cur] = False
    cnt = 0

    for k in flight[cur]:
        if country[k]:
            cnt += dfs(country, flight, k) + 1

    return cnt

for i in range(T):
    N, M = map(int, input().split())
    countries = [True] * (N+1)
    countries[0] = False
    flights = defaultdict(list)


    for j in range(M):
        a, b = map(int, input().split())
        flights[a].append(b)
        flights[b].append(a)

    tmp = dfs(countries, flights, 1)
    result.append(tmp)

print(*result, sep="\n")
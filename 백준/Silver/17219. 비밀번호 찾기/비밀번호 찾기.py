import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
add_pw = {}

for i in range(N):
    address, password = map(str, input().split())
    add_pw[address] = password

for j in range(M):
    find = str(input().rstrip())
    temp = add_pw[find]
    result.append(temp)

for r in result:
    print(r)

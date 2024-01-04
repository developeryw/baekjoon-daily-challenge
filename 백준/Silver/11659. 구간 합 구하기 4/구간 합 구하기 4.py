import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num_arr = [0]

for k in range(1, N+1):
    tmp = num[k-1] + num_arr[k-1]
    num_arr.append(tmp)

result = []

for k in range(M):
    i, j = map(int, input().split())
    tmp = num_arr[j] - num_arr[i-1]
    result.append(tmp)

for r in result:
    print(r)
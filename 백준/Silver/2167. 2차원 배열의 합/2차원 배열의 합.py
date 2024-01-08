import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_arr = [[0] * (M+1)]
for _ in range(N):
    temp = list(map(int, input().split()))
    temp.insert(0, 0)
    num_arr.append(temp)

new_num_arr = [[0] * (M+1) for _ in range(N+1)]

for n in range(1, N+1):
    for m in range(1, M+1):
        new_num_arr[n][m] = new_num_arr[n-1][m] + new_num_arr[n][m-1] - new_num_arr[n-1][m-1] + num_arr[n][m]

K = int(input())
result = []
for k in range(K):
    i, j, x, y = map(int, input().split())
    answer = new_num_arr[x][y] - new_num_arr[x][j-1] - new_num_arr[i-1][y] + new_num_arr[i-1][j-1]
    result.append(answer)

for r in result:
    print(r)
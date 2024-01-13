import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num_arr = [True] * (N+1)
cur = 0
cnt = 0

for i in range(2, N+1):
        for j in range(i, N+1, i):
            if cnt == K:
                break

            if num_arr[j]:
                num_arr[j] = False
                cur = j
                cnt += 1

print(cur)
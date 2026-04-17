import sys
input = sys.stdin.readline

N = int(input())
max_num = 10000

cnt_list = [0] * (max_num + 1)

for i in range(N):
    num = int(input())
    cnt_list[num] += 1

for j in range(max_num + 1):
    for k in range(cnt_list[j]):
        print(j)
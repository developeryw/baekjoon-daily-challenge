import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num_lst = deque(sorted(set(num)))
new_num = {}

for i in range(len(num_lst)):
    cur = num_lst.popleft()
    if cur not in new_num.keys():
        new_num[cur] = i

for n in num:
    print(new_num[n], end=" ")
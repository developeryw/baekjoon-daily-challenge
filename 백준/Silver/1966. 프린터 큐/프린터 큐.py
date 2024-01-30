import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
result = []

def check_importance(dq, index_list, target):
    cnt = 0
    maximum = max(dq)

    front = dq.popleft()
    cur = index_list.popleft()

    checking = -1

    while True:
        if maximum > front:
            dq.append(front)
            index_list.append(cur)
        else:
            cnt += 1
            checking = cur

            if checking == target:
                break

            maximum = max(dq)

        front = dq.popleft()
        cur = index_list.popleft()

    return cnt

for i in range(T):
    N, M = map(int, input().split())
    num_lst = deque(map(int, input().split()))
    idx_lst = deque([num for num in range(N)])

    answer = check_importance(num_lst, idx_lst, M)
    result.append(answer)

print(*result, sep="\n")
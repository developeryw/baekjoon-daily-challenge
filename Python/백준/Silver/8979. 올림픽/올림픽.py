import sys
input = sys.stdin.readline

N, K = map(int, input().split())

olympic = [list(map(int, input().split())) for _ in range(N)]
rank, tied = 1, 0

olympic = sorted(olympic, key= lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(0, N): 
    if i:
        if olympic[i][1:] == olympic[i-1][1:]:
            tied += 1
        else:
            rank += (tied + 1)
            tied = 0

    if olympic[i][0] == K:
        print(rank)
        break
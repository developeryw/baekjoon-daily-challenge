import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = []
result = []

for i in range(N):
    tmp = list(map(str, input().rstrip()))
    chess.append(tmp)

for j in range(N-8+1):
    for k in range(M-8+1):
        start_black = 0
        start_white = 0

        for n in range(j, j+8):
            for m in range(k, k+8):
                cur = n + m
                if cur % 2 == 0:
                    if chess[n][m] != 'B':
                        start_black += 1
                    else:
                        start_white += 1
                else:
                    if chess[n][m] != 'W':
                        start_black += 1
                    else:
                        start_white += 1

        result.append(start_black)
        result.append(start_white)

print(min(result))
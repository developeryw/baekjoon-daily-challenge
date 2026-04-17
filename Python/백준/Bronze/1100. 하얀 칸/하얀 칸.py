import sys
input = sys.stdin.readline

chess = []
result = 0

for i in range(8):
    tmp = list(map(str, input()))
    chess.append(tmp)
    
for j in range(0, 8):
    for k in range(0, 8):
        if (j+k) % 2 == 0 and chess[j][k] == 'F':
            result += 1

print(result)
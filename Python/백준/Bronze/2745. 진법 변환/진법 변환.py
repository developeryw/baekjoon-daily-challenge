import sys
input = sys.stdin.readline

N, B = input().split()
B = int(B)
N = list(N)

total = 0

for i in range(len(N)):
    if '0' <= N[i] <= '9':
        total += int(N[i]) * (B ** (len(N) - i - 1))
    elif 'A' <= N[i] <= 'Z':
        total += (ord(N[i]) - 55) * (B ** (len(N) - i - 1))

print(total)
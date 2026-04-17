import sys
input = sys.stdin.readline

N = int(input())
result = 0

for _ in range(N):
    plug = int(input())
    result += plug
    
print(result - N + 1)
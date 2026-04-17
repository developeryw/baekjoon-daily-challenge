import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

result = 0

for i in range(N):
    if num[i] != (i+1):
        result += 1
        
print(result)
import sys
input = sys.stdin.readline

n, k, p = map(int, input().split())
bread = list(map(int, input().split()))

result = 0

for i in range(0, n, k):
    if sum(bread[i:i+k]) > (k - p):
        result += 1
        
print(result)
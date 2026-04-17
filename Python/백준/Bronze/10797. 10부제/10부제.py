import sys
input = sys.stdin.readline

N = int(input())
cars = list(map(int, input().split()))

result = 0

for i in cars:
    if i % 10 == N:
        result += 1
        
print(result)
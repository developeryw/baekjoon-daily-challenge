import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
miles = deque(map(int, input().split()))
prices = deque(map(int, input().split()))

minimum = prices[0]

total = 0

for i in range(N-1):
    if prices[i] < minimum:
        minimum = prices[i]
    
    total += minimum * miles[i]

print(total)
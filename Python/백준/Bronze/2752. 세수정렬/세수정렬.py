import sys
from collections import deque
input = sys.stdin.readline

num = sorted(list(map(int, input().split())))

for n in num:
    print(n, end=' ')
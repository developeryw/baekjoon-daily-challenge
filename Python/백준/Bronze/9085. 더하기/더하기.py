import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    
    print(sum(lst))
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(str, input().split())
    a = int(a)
    
    print(b * a)
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    name = input().rstrip()
    
    name = name.lower()
    print(name)
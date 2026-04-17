import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    beauty = set()
    num = input().rstrip()
    
    for n in num:
        beauty.add(n)
    
    print(len(beauty))
    
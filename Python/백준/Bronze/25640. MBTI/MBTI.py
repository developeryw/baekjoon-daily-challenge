import sys
input = sys.stdin.readline

jinho = input().rstrip()
n = int(input())
result = 0

for _ in range(n):
    friend = input().rstrip()
    
    if jinho == friend:
        result += 1
        
print(result)
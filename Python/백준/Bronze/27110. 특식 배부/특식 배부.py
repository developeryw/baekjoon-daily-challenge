import sys
input = sys.stdin.readline

n = int(input())
chicken = list(map(int, input().split()))

result = 0
               
for i in range(3):
    if chicken[i] - n >= 0:
        result += n
    else:
        result += chicken[i]
        
print(result)
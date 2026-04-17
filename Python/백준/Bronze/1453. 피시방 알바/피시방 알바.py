import sys
input = sys.stdin.readline

N = int(input())
customer = list(map(int, input().split()))
pc = [-1] * 100

for i in customer:
    pc[i-1] += 1
    
for j in range(100):
    if pc[j] == -1:
        pc[j] += 1
        
print(sum(pc))
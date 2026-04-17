import sys
input = sys.stdin.readline

hat = []

for _ in range(9):
    num = int(input())
    hat.append(num)
    
for i in range(len(hat)):
    for j in range(i+1, len(hat)):
        if sum(hat) - hat[i] - hat[j] == 100:
            hat.pop(j)
            hat.pop(i)
            break
            
hat.sort()
print(*hat, sep="\n")
import sys
input = sys.stdin.readline

n = int(input())
d = 0
p = 0

for _ in range(n):
    result = input().rstrip()
        
    if abs(d-p) >= 2:
        break
    else:
        if result == "D":
            d += 1
        else:
            p += 1
            
print(d, ":", p, sep="")
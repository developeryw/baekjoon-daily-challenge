import sys
input = sys.stdin.readline

remainder = {}

for i in range(10):
    temp = int(input())
    temp %= 42

    if temp not in remainder:
        remainder[temp] = 1
    else:
        remainder[temp] += 1
        
print(len(remainder))

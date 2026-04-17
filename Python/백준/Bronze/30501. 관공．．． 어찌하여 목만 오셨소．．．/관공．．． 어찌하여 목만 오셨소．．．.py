import sys
input = sys.stdin.readline

n = int(input())
name_arr = []

for _ in range(n):
    name = input().rstrip()
    name_arr.append(name)
    
for i in name_arr:
    if 'S' in i:
        print(i)
        break
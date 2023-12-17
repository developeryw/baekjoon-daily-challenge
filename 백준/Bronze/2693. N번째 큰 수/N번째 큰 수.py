import sys
input = sys.stdin.readline

T = int(input())
result = []

for i in range(T):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    
    result.append(arr[2])

for r in result:
    print(r)
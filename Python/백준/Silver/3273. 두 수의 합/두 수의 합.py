import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

result = 0

left = 0
right = n - 1

arr.sort()

while left < right:
    cur = arr[left] + arr[right]

    if cur == x:
        result += 1
        left += 1
        right -= 1
    elif cur > x:
        right -= 1
    else:
        left += 1
    
print(result)

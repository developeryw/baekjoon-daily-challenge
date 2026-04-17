import sys
input = sys.stdin.readline

arr = input().rstrip()

if arr[0] == '"' and arr[-1] == '"' and len(arr) > 2:
    print(arr[1:len(arr)-1])
else:
    print("CE")
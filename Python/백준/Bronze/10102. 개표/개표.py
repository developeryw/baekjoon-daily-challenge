import sys
input = sys.stdin.readline

n = int(input())
arr = input().rstrip()

for i in arr:
    if i == "A":
        n -= 1
        
if len(arr) - n < n:
    print("B")
elif len(arr) - n > n:
    print("A")
else:
    print("Tie")
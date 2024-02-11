import sys
input = sys.stdin.readline

n = int(input())
stack = []
num_arr = []
cur = 1
idx = 0
result = []

for i in range(n):
    tmp = int(input())
    num_arr.append(tmp)

while True:
    if idx >= n:
        print(*result, sep="\n")
        break

    if cur <= num_arr[idx]:
        stack.append(cur)
        cur += 1
        result.append("+")
    elif num_arr[idx] == stack[-1]:
        stack.pop()
        idx += 1
        result.append("-")
    else:
        result = []
        print("NO")
        break
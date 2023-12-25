import sys
input = sys.stdin.readline

N = int(input())
x_arr = []
y_arr = []

for i in range(N):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

x_arr.sort()
y_arr.sort()

W = x_arr[-1] - x_arr[0]
H = y_arr[-1] - y_arr[0]

print(W * H)
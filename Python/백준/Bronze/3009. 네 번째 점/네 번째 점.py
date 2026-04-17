import sys
input = sys.stdin.readline

rectangle_x = {}
rectangle_y = {}

for i in range(3):
    x, y = map(int, input().split())

    if x in rectangle_x:
        rectangle_x[x] += 1
    else:
        rectangle_x[x] = 1

    if y in rectangle_y:
        rectangle_y[y] += 1
    else:
        rectangle_y[y] = 1

X = 0
Y = 0

for j in rectangle_x:
    if rectangle_x[j] % 2 != 0:
        X = j

for k in rectangle_y:
    if rectangle_y[k] % 2 != 0:
        Y = k

print(X, Y)
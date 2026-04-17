import sys
input = sys.stdin.readline

row_index = 0
column_index = 0

number = [[0 for i in range(9)] for j in range(9)]

for x in range(0, 9, 1):
    line = list(map(int, input().split()))
    number[x] = line

max_num = number[0][0]

for y in range(0, 9, 1):
    for z in range(0, 9, 1):
        if max_num < number[y][z]:
            max_num = number[y][z]
            row_index = y
            column_index = z

print(max_num)
print(row_index+1, column_index+1)
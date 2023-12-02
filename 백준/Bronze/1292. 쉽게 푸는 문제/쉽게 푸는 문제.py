import sys
input = sys.stdin.readline

A, B = map(int, input().split())
num = 1
num_lst = []
total = 0

while len(num_lst) < B:
    for i in range(num):
        num_lst.append(num)

    num += 1

for j in range(A-1, B):
    total += num_lst[j]

print(total)
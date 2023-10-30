import sys
input = sys.stdin.readline

num_lst = list(map(int, input().split()))
num_lst = sorted(num_lst)

width = num_lst[2]
height = num_lst[0]

print(width * height)
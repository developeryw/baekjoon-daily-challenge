import sys
input = sys.stdin.readline

N = int(input())
N_card = list(map(int, input().split()))

M = int(input())
M_card = list(map(int, input().split()))

cnts = {}

for j in N_card:
    if j in cnts:
        cnts[j] += 1
    else:
        cnts[j] = 1

for k in M_card:
    if k in cnts:
        print(cnts[k], end=" ")
    else:
        print(0, end=" ")

import sys
input = sys.stdin.readline

A, B = map(list, input().split())
index = 2

for i in range(0, 3, 1):
    if A[index] > B[index]:
        for j in range(2, -1, -1):
            print(A[j], end="")
        break
    elif A[index] < B[index]:
        for j in range(2, -1, -1):
            print(B[j], end="")
        break
    else:
        index -= 1
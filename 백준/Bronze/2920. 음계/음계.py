import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
isAscending = [1, 2, 3, 4, 5, 6, 7, 8]
isDescending = [8, 7, 6, 5, 4, 3, 2, 1]

if num == isAscending:
    print("ascending")
elif num == isDescending:
    print("descending")
else:
    print("mixed")
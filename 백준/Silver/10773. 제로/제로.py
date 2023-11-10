import sys
input = sys.stdin.readline

K = int(input())
lst = []
sum = 0

for i in range(K):
    num = int(input())

    if num != 0:
        lst.append(num)
    else:
        del lst[-1]

for j in lst:
    sum += j

print(sum)
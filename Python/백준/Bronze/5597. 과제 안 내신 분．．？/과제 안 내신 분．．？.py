import sys
input = sys.stdin.readline

numarr = [0] * 31

for i in range(0, 28, 1):
    tmp = int(input())
    numarr[tmp] = 1

for j in range(1, 31, 1):
    if numarr[j] == 0:
        print(j, end=" ")
import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

number = A * B * C
number = str(number)

for i in range(0, 10):
    cnt = number.count(str(i))
    print(cnt)
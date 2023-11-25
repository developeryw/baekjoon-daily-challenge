import sys
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

korean = A / C
mathematics = B / D

if A % C != 0:
    korean += 1

if B % D != 0:
    mathematics += 1

maximum = int(max(korean, mathematics))

print(L - maximum)
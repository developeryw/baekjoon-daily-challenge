import sys
input = sys.stdin.readline

N = int(input())

start = 1
mul = 1
room = 1

while start < N:
    start += (mul * 6)
    mul += 1
    room += 1

print(room)

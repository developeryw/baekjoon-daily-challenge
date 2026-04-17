import sys
input = sys.stdin.readline

L, P = map(int, input().split())
num = list(map(int, input().split()))
people = L * P

for i in range(len(num)):
    num[i] -= people

print(*num)
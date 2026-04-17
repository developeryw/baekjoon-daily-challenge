import sys
input = sys.stdin.readline

n = int(input())

week = 7 * 24 * 60 * 60
result = 1

for i in range(1, n+1):
    result *= i

print(result // week)
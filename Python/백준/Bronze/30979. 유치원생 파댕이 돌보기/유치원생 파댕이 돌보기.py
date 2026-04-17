import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
taste = list(map(int, input().split()))

if sum(taste) >= t:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
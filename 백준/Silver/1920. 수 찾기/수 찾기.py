import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

result = [1 if x in A else 0 for x in B]

for k in result:
    print(k)
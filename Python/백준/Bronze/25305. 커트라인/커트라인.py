import sys
input = sys.stdin.readline

N, k = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)

print(num[k-1])

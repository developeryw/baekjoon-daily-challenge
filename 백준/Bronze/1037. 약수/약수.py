import sys
input = sys.stdin.readline

N = int(input())
measure = list(map(int, input().split()))
measure = sorted(measure)

print(measure[0] * measure[N-1])
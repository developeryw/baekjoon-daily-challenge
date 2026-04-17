import sys
input = sys.stdin.readline

w, h = map(int, input().split())

print(round(w * h * 0.5, 1))
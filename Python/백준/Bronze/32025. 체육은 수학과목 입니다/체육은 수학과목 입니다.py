import sys
input = sys.stdin.readline

h = int(input())
w = int(input())

print(int(min(h, w) / 2 * 100))
import sys
input = sys.stdin.readline

i1, m1, s1, e1 = map(int, input().split())
i2, m2, s2, e2 = map(int, input().split())

minkook = i1 + m1 + s1 + e1
manse = i2 + m2 + s2 + e2

print(max(minkook, manse))
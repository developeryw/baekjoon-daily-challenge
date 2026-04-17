import sys
input = sys.stdin.readline

n = int(input())
call = list(map(int, input().split()))
input()

y = 0
m = 0

for i in call:
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15

if y > m:
    print("M", m)
elif y == m:
    print("Y", "M", y)
else:
    print("Y", y)
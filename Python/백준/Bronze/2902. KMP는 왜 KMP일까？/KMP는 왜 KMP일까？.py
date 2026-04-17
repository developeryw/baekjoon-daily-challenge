import sys
input = sys.stdin.readline

kmp = list(map(str, input().split("-")))

for l in kmp:
    print(l[0], end="")

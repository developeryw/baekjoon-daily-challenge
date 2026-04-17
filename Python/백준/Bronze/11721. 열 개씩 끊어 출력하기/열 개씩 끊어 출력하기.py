import sys
input = sys.stdin.readline

word = input().rstrip()
next = 0

for i in word:
    if next == 10:
        next = 0
        print()
    
    print(i, end="")
    next += 1
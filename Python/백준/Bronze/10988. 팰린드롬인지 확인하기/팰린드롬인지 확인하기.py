import sys
input = sys.stdin.readline

word = input().strip()
is_true = 1
j = len(word)
index = 0

for i in range(0, j//2+1, 1):
    if not word[i] == word[j-1-i]:
        is_true = 0

print(is_true)
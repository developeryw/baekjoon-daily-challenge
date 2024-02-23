import sys
input = sys.stdin.readline

S = list(map(str, input().rstrip()))
result = [0] * 26

for letter in S:
    result[ord(letter) - 97] += 1

print(*result, sep=" ")
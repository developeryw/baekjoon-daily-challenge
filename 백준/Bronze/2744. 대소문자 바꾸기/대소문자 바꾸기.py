import sys
input = sys.stdin.readline

word = list(map(str, input().rstrip()))

for i in range(len(word)):
    asc = ord(word[i])
    if asc >= 97:
        word[i] = chr(asc - 32)
    else:
        word[i] = chr(asc + 32)

print(*word, sep="")
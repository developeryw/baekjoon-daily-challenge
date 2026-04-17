import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

letter = {}
cnt = 0

for txt in str1:
    if txt in letter:
        letter[txt] += 1
    else:
        letter[txt] = 1

for txt in str2:
    if txt in letter:
        letter[txt] -= 1
    else:
        cnt += 1

for txt in letter:
    if letter[txt] > 0:
        cnt += letter[txt]
    elif letter[txt] < 0:
        cnt -= letter[txt]

print(cnt)
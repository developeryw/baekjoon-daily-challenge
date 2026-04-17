import sys
input = sys.stdin.readline

word = input()
alphabet = 0
dz_cnt = 0

for i in range(1, len(word)):
    if word[i] == '=':
        if word[i-1] == 'c' or word[i-1] == 'z' or word[i-1] == 's':
            alphabet += 1
    elif word[i] == '-':
        if word[i-1] == 'c' or word[i-1] == 'd':
            alphabet += 1
    elif word[i] == 'j':
        if word[i-1] == 'l' or word[i-1] == 'n':
            alphabet += 1

for j in range(2, len(word)):
    if word[j-2] == 'd' and word[j-1] == 'z' and word[j] == '=':
        dz_cnt += 1

alphabet += len(word) - 1 - alphabet * 2 - dz_cnt

print(alphabet)
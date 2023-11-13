import sys
input = sys.stdin.readline

n = int(input())
group_words = 0

for i in range(n):
    cnt = [0] * 26
    isGroup = 0
    word = input()

    for j in range(1, len(word) - 1):
        if j == 1:
            cnt[ord(word[j-1]) - 97] += 1

        if word[j] != word[j-1]:
            if cnt[ord(word[j]) - 97] >= 1:
                cnt[ord(word[j]) - 97] = -100
            else:
                cnt[ord(word[j]) - 97] += 1

    for k in range(len(cnt)):
        if cnt[k] >= 0:
            isGroup += 1

    if isGroup == 26:
        group_words += 1

print(group_words)
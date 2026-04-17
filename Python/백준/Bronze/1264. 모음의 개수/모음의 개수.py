import sys
input = sys.stdin.readline

result = []
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while True:
    sentence = str(input().rstrip())
    cnt = 0

    if sentence == "#":
        print(*result, sep="\n")
        break
    
    for i in sentence:
        if i in vowel:
            cnt += 1

    result.append(cnt)
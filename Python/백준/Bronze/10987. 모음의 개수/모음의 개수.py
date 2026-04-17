import sys
input = sys.stdin.readline

word = input().rstrip()
result = 0

for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        result += 1
        
print(result)
import sys
input = sys.stdin.readline
from collections import deque

name = list(input().rstrip())
alphabet =  {}

for a in name:
    if a in alphabet:
        alphabet[a] += 1
    else:
        alphabet[a] = 1

odd = 0
center = ""

for b in alphabet:
    if alphabet[b] % 2 != 0:
        odd += 1
        center = b
    
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    alphabet = dict(sorted(alphabet.items(), key = lambda x: x[0], reverse=True))
    string = deque()

    if center:
        string.append(center)
    
    for c in alphabet:
        for _ in range(alphabet[c] // 2):
            string.appendleft(c)
            string.append(c)
    
    print(*string, sep="")
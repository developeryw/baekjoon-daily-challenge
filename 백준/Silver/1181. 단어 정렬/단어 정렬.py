import sys
input = sys.stdin.readline

N = int(input())
dictionary = set()

for i in range(N):
    word = input().rstrip()
    dictionary.add(word)

def sorting(word):
    return (len(word), word)

dictionary = sorted(dictionary, key=sorting)

for d in dictionary:
    print(d)
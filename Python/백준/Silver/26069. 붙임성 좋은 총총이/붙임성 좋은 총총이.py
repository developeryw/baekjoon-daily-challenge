import sys
input = sys.stdin.readline

T = int(input())
dance = set()
dance.add("ChongChong")

for _ in range(T):
    a, b = map(str, input().rstrip().split())

    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))
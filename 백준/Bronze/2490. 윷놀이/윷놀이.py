import sys
input = sys.stdin.readline

result = []

def judge(lst):
    if lst.count(1) == 3:
        return "A"
    elif lst.count(1) == 2:
        return "B"
    elif lst.count(1) == 1:
        return "C"
    elif lst.count(1) == 4:
        return "E"
    else:
        return "D"

for i in range(3):
    playing = list(map(int, input().split()))
    temp = judge(playing)
    result.append(temp)

for r in result:
    print(r)
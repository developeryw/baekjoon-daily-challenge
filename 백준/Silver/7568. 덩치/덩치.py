import sys
input = sys.stdin.readline

N = int(input())
people = []

for i in range(N):
    w, h = map(int, input().split())
    temp = {'weight': w, 'height': h, 'index': i}
    people.append(temp)

rankings = []

for j in range(N):
    rank = 1

    for k in range(N):
        if people[k]['weight'] > people[j]['weight'] and people[j]['height'] < people[k]['height']:
            rank += 1

    rankings.append(rank)

for r in rankings:
    print(r, end=" ")
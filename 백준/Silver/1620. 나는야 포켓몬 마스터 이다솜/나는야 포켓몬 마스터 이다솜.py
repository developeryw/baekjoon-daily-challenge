import sys
input = sys.stdin.readline

pocketmon = {}
result = []

N, M = map(int, input().split())

for i in range(1, N+1):
    pocketmon[str(i)] = input().rstrip()

re_pocketmon = dict(map(reversed, pocketmon.items()))

for j in range(M):
    quiz = input().rstrip()

    if quiz in pocketmon:
        answer = pocketmon[quiz]
        result.append(answer)
    else:
        answer = re_pocketmon[quiz]
        result.append(answer)

for k in result:
    print(k)
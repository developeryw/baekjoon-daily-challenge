import sys
input = sys.stdin.readline

def bingo(lst):
    cnt = 0

    diagonal1 = lst[0][0] + lst[1][1] + lst[2][2] + lst[3][3] + lst[4][4]
    diagonal2 = lst[0][4] + lst[1][3] + lst[2][2] + lst[3][1] + lst[4][0]

    for i in range(5):
        if sum(lst[i]) == 0:
            cnt += 1

    for j in range(5):
        tmp = 0

        for k in range(5):
            tmp += lst[k][j]
        
        if tmp == 0:
            cnt += 1
    
    if diagonal1 == 0:
        cnt += 1

    if diagonal2 == 0:
        cnt += 1

    return cnt 

cheolsu = []
game = []

cur = 0

for i in range(5):
    line = list(map(int, input().split()))
    cheolsu.append(line)

for j in range(5):
    order = list(map(int, input().split()))

    for k in range(5):
        game.append(order[k])

while True:
    for i in range(5):
        for j in range(5):
            if cheolsu[i][j] == game[cur]:
                cheolsu[i][j] = 0

    if bingo(cheolsu) >= 3:
        print(cur + 1)
        break

    cur += 1 

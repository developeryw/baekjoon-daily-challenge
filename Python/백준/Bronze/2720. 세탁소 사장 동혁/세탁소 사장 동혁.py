import sys
input = sys.stdin.readline

def cal_change(cash, price):
    cnt = price // cash
    last = price % cash

    lst = list()
    lst.append(cnt)
    lst.append(last)

    return lst

T = int(input())
C = 0
change_list = list()

for i in range(0, T, 1):
    C = int(input())

    temp1 = cal_change(25, C)
    last1 = int(temp1[1])

    temp2 = cal_change(10, last1)
    last2 = int(temp2[1])

    temp3 = cal_change(5, last2)
    last3 = int(temp3[1])

    temp4 = cal_change(1, last3)

    change_list.append([int(temp1[0]), int(temp2[0]), int(temp3[0]), int(temp4[0])])

for j in range(len(change_list)):
    for k in range(len(change_list[j])):
        print(change_list[j][k], end=" ")
    print()
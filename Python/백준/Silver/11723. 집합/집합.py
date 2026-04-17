import sys
input = sys.stdin.readline

N = int(input())
x = [False] * 21

def calculator(Cal, Num, X):
    if Cal == 'add':
        X[Num] = True
    elif Cal== 'remove':
        X[Num] = False
    elif Cal == 'check':
        if X[Num]:
            print(1)
        else:
            print(0)
    elif Cal == 'toggle':
        X[Num] = not X[Num]
    elif Cal == 'all':
        for i in range(1, 21):
            X[i] = True
    elif Cal == 'empty':
        for i in range(1, 21):
            X[i] = False

    return X

for i in range(N):
    lst = list(map(str, input().split()))
    cal = lst[0]
    if len(lst) > 1:
        num = int(lst[1])
    else:
        num = 0
    x = calculator(cal, num, x)
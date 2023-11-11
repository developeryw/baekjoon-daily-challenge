import sys
input = sys.stdin.readline

N = int(input())
num_list = []
result = []

def menu(n, stack, order):
    if n == 1:
        stack.append(order[1])
    elif n == 2:
        if len(stack) > 0:
            result.append(stack.pop(-1))
        else:
            result.append(-1)
    elif n == 3:
        result.append(len(stack))
    elif n == 4:
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif n == 5:
        if len(stack) > 0:
            result.append(stack[-1])
        else:
            result.append(-1)

    return stack

for count in range(N):
    order_list = list(map(int, input().split()))
    menu_num = order_list[0]

    num_list = menu(menu_num, num_list, order_list)

for r in result:
    print(r)
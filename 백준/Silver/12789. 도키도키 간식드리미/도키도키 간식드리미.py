import sys
input = sys.stdin.readline

N = int(input())
current_line = list(map(int, input().split()))
current_line = [current_line[n] for n in range(N-1, -1, -1)]

order = 1
temp_line = []

def order_pop(order_num):
    if len(current_line) > 0 and current_line[-1] == order_num:
        del current_line[-1]
        order_num += 1
    elif len(temp_line) > 0 and temp_line[-1] == order_num:
        del temp_line[-1]
        order_num += 1
    else:
        if len(current_line) == 0:
            return 0
        else:
            temp_line.append(current_line[-1])
            del current_line[-1]

    return order_num

while order <= N:
    if order == 0:
        break

    order = order_pop(order)

if order == 0:
    print("Sad")
else:
    print("Nice")
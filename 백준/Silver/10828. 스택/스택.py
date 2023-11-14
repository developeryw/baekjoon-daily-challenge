import sys
input = sys.stdin.readline

N = int(input())
stack = []

def stack_instruction(inst):
    menu = inst[0]

    if menu == 'push':
        stack.append(int(inst[1]))
    elif menu == 'pop':
        if stack:
            num = stack.pop()
            print(num)
        else:
            print(-1)
    elif menu == 'size':
        print(len(stack))
    elif menu == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif menu == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

for i in range(N):
    instruction = list(input().split())
    stack_instruction(instruction)
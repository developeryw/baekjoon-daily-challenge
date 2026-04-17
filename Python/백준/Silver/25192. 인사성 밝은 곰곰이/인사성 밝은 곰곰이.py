import sys
input = sys.stdin.readline

N = int(input())
chat = {}
enter = 0
result = 0

for _ in range(N):
    arr = input().rstrip()

    if arr == "ENTER":
        enter += 1
    else:
        if arr in chat:
            if chat[arr] < enter:
                result += 1
                chat[arr] = enter
        else:
            result += 1
            chat[arr] = enter
            
print(result)
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

def judge(number):
    istrue = 1
    for i in range(len(number)-3, -1, -1):
        if number[i] - number[i+1] == number[i+1] - number[i+2]:
            istrue = 1
        else:
            istrue = 0
            break

    return istrue

while N > 0:
    num_arr = list(map(int, str(N)))
    cnt += judge(num_arr)
    N -= 1

print(cnt)
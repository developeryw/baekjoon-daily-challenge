import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
switch = deque(map(int, input().split()))
switch.appendleft(0)

n = int(input())

def male(num):
    for j in range(num, len(switch), num):
        switch[j] = (switch[j] + 1) % 2

def female(num):
    start = num
    end = num
    minimum = min(num - 1, N - num)

    for k in range(1, minimum + 1):
        if switch[num+k] != switch[num-k]:
            break
        else:
            start = num - k
            end = num + k

    for l in range(start, end+1):
        switch[l] = (switch[l] + 1) % 2

for i in range(n):
    sex, number = map(int, input().split())
    if sex == 1:
        male(number)
    else:
        female(number)

switch.popleft()

for s in range(0, N):
    if s % 20 == 0 and s > 0:
        print("")

    print(switch[s], end=" ")

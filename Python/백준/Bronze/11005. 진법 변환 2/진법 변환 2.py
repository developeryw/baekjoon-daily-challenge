import sys
input = sys.stdin.readline

N, B = map(int, input().split())
arr = list()

while N >= B:
    remainder = N % B
    if 9 < remainder < 36:
        arr.append(chr(remainder + 55))
    else:
        arr.append(str(remainder))

    N = N // B
    
if 9 < N < 36:
    arr.append(chr(N + 55))
else:
    arr.append(str(N))

for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end="")
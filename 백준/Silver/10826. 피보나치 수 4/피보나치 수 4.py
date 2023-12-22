import sys
input = sys.stdin.readline

N = int(input())
fibonacci = [0, 1]

for i in range(2, N+1):
    temp = fibonacci[i-2] + fibonacci[i-1]
    fibonacci.append(temp)

print(fibonacci[N])
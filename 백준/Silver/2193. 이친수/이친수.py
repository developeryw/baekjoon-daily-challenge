import sys
input = sys.stdin.readline

N = int(input())
fibonacci = [1, 1]

for i in range(2, N):
    number = fibonacci[i-2] + fibonacci[i-1]
    fibonacci.append(number)

print(fibonacci[N-1])
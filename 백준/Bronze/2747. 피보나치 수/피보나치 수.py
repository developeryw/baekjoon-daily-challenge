import sys
input = sys.stdin.readline

n = int(input())
fibonacci = [0, 1]

for i in range(2, n+1):
    temp = fibonacci[i-2] + fibonacci[i-1]
    fibonacci.append(temp)

print(fibonacci[n])
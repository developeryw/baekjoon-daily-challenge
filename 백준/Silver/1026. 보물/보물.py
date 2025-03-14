import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

for i in range(N):
    max_a = max(A)
    min_b = min(B)

    result += max_a * min_b

    A.pop(A.index(max_a))
    B.pop(B.index(min_b))

print(result)
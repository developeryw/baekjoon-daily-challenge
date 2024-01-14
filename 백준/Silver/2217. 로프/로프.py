import sys
input = sys.stdin.readline

N = int(input())
ropes = []
result = []

for i in range(N):
    rope = int(input())
    ropes.append(rope)

ropes.sort(reverse=True)

for j in range(N):
    result.append(ropes[0] * (j+1))
    del ropes[0]

print(max(result))
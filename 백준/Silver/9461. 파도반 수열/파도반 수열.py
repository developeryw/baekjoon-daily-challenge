import sys
input = sys.stdin.readline

P = [1, 1, 1]

T = int(input())
N = []
for i in range(T):
    tmp = int(input())
    N.append(tmp)

maximum = max(N)

for j in range(maximum - 3):
    element = P[j] + P[j+1]
    P.append(element)

for k in N:
    print(P[k-1])
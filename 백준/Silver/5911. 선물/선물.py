import sys
input = sys.stdin.readline

N, B = map(int, input().split())
P = []
S = []
result = []

for i in range(N):
    p, s = map(int, input().split())
    P.append(p)
    S.append(s)

for j in range(N):
    total = 0
    cnt = 0
    PS = []

    for k in range(N):
        if j == k:
            PS.append(P[k] / 2 + S[k])
        else:
            PS.append(P[k] + S[k])
            
    PS.sort()
            
    for l in range(N):
        total += PS[l]
        
        if total > B:
            break
            
        cnt += 1
        
    result.append(cnt)
    
print(max(result))
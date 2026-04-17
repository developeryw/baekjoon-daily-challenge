import sys
input = sys.stdin.readline

a, b = map(str, input().split())

a1 = ""
b1 = ""

a2 = ""
b2 = ""

for i in range(len(a)):
    if a[i] == '5':
        a1 += '6'
        a2 += '5'
    elif a[i] == '6':
        a2 += '5'
        a1 += '6'
    else:
        a1 += a[i]
        a2 += a[i]
        
for j in range(len(b)):
    if b[j] == '5':
        b1 += '6'
        b2 += '5'
    elif b[j] == '6':
        b2 += '5'
        b1 += '6'
    else:
        b1 += b[j]
        b2 += b[j]
        
print(int(a2) + int(b2), int(a1) + int(b1))
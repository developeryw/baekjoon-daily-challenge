import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())
bigger = max(num1, num2)
G = 0
L = 1

for i in range(1, bigger+1):
    if num1 % i == 0 and num2 % i == 0:
        G = i

divisor = 2
cnt1 = 0
cnt2 = 0

while divisor <= bigger:
    if num1 % divisor == 0:
        num1 = num1 // divisor
        cnt1 += 1
    elif num2 % divisor == 0:
        num2 = num2 // divisor
        cnt2 += 1
    else:
        exponent = max(cnt1, cnt2)
        L = L * (divisor ** exponent)

        cnt1 = 0
        cnt2 = 0
        divisor += 1

print(G)
print(L)
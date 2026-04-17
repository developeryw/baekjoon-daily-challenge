import sys
input = sys.stdin.readline

skills = list(map(int, input().split()))
minimum = 100000

for i in range(3):
    for j in range(i+1, 4):
        tmp = skills[i] + skills[j]
        tmp2 = sum(skills) - tmp * 2

        if abs(tmp2) < minimum:
            minimum = abs(tmp2)
            
print(minimum)
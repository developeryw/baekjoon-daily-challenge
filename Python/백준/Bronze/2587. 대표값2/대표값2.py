import sys
input = sys.stdin.readline

number = []
total = 0

for i in range(5):
    temp = int(input())
    number.append(temp)
    total += temp

number = sorted(number)

print(int(total / 5))
print(number[2])
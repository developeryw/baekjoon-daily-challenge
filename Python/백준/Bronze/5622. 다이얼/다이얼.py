import sys
input = sys.stdin.readline

number = input()
time = 0

for i in range(0, len(number), 1):
    temp = ord(number[i])-65

    if 0 <= temp < 3:
        time += 3
    elif 3 <= temp < 6:
        time += 4
    elif 6 <= temp < 9:
        time += 5
    elif 9 <= temp < 12:
        time += 6
    elif 12 <= temp < 15:
        time += 7
    elif 15 <= temp < 19:
        time += 8
    elif 19 <= temp < 22:
        time += 9
    elif 22 <= temp < 26:
        time += 10
    else:
        continue

print(time)
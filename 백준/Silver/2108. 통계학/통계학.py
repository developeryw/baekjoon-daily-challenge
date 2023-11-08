import sys
input = sys.stdin.readline

N = int(input())

num_list = []
sum = 0
occur = {}

for i in range(N):
    number = int(input())
    num_list.append(number)
    sum += number

    if number in occur:
        occur[number] += 1
    else:
        occur[number] = 1

mean = round(sum / N)

num_list.sort()
if N % 2 == 0:
    median = (num_list[N // 2 - 1] + num_list[N//2]) / 2
else:
    median = num_list[N // 2]

max_occur = max(occur.values())
mode_list = [num for num, count in occur.items() if count == max_occur]
mode_list.sort()

if len(mode_list) > 1:
    mode = mode_list[1]
else:
    mode = mode_list[0]

Range = max(num_list) - min(num_list)

print(mean)
print(median)
print(mode)
print(Range)

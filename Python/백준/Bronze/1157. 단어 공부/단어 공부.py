import sys
input = sys.stdin.readline

arr = input()

cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0]

for i in range(len(arr)):
    temp = arr[i]
    if 65 <= ord(arr[i]) <= 90:
        temp = ord(arr[i]) - 65
        cnt[temp] += 1
    elif 97 <= ord(arr[i]) <= 122:
        temp = ord(arr[i]) - 97
        cnt[temp] += 1

max_num = max(cnt)
max_count = cnt.count(max_num)

if max_count > 1:
    print("?")
else:
    print(chr(cnt.index(max_num) + 65))

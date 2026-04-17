import sys
input = sys.stdin.readline

string = input().rstrip()
cnt = 0

for i in range(0, len(string) - 3):
    if string[i:i+4] == "DKSH":
        cnt += 1

print(cnt)
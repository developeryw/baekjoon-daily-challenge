import sys
input = sys.stdin.readline

n = int(input())
friends = list(map(str, input().rstrip().split()))
hellobit = input().rstrip()

result = 0

for friend in friends:
    if friend == hellobit:
        result += 1
        
print(result)
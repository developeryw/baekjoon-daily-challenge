import sys
input = sys.stdin.readline

n = int(input())
company = {}

for i in range(n):
    name, record = map(str, input().split())
    if record == "enter":
        company[name] = 1
    elif record == "leave":
        company[name] = 0

result = [key for key, value in company.items() if value == 1]
result.sort(reverse=True)

for r in result:
    print(r)
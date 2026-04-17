import sys
input = sys.stdin.readline

arr = input().rstrip().split(".")
result = ""

for text in arr:
    if text and len(text) % 2 == 0:
        result += ("AAAA" * (len(text) // 4))

        if len(text) % 4 == 2:
            result += "BB"
    elif len(text) % 2 != 0:
        print(-1)
        exit(0)

    result += "."


if result:
    print(result[:len(result) - 1])
else:
    print(-1)
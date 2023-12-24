import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
triangle = [a, b, c]
triangle.sort()

while triangle[0] + triangle[1] <= triangle[2]:
    triangle[2] -= 1

print(triangle[0] + triangle[1] + triangle[2])
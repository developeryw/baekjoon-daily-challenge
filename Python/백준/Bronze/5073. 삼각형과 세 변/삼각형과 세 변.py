import sys
input = sys.stdin.readline

def isISO(num1, num2, num3):
    if num1 == num2 and num1 != num3:
        return 1
    else:
        return 0

while True:
    line1, line2, line3 = map(int, input().split())
    longest = max(line1, line2, line3)

    if line1 == 0 and line2 == 0 and line3== 0:
        break

    if longest >= ((line1 + line2 + line3) - longest):
        print("Invalid")
        continue

    if line1 == line2 and line2 == line3:
        print("Equilateral")
    elif isISO(line1, line2, line3) == 1 or isISO(line2, line3, line1) == 1 or isISO(line3, line1, line2) == 1:
        print("Isosceles")
    elif line1 != line2 and line2 != line3 and line3 != line1:
        print("Scalene")
import sys
input = sys.stdin.readline

numbers = []

while True:
    n = input().strip()
    
    if n == "":
        break
    
    numbers.append(int(n))

for n in numbers:
    number = 1
    length = 1

    while True:
        if number % n == 0:
            print(length)
            break

        number += 10 ** length
        length += 1
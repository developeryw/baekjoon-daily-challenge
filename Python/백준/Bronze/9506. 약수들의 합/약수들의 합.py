import sys
input = sys.stdin.readline

divisor_lst = []
N = []

while True:
    n = int(input())
    divisor_sum = 0

    if n == -1:
        break

    N.append(n)
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
            divisors.append(i)

    if divisor_sum == n:
        divisor_lst.append(divisors)
    else:
        divisor_lst.append([])

result = [[] for _ in range(len(N))]

for j in range(0, len(divisor_lst)):
    if len(divisor_lst[j]) == 0:
        result[j].append(str(N[j]) + " is NOT perfect.")
    else:
        result[j].append(str(N[j]) + " = " + " + ".join(map(str, divisor_lst[j])))

for m in result:
    temp = str(m)[2:-2]
    print(temp)
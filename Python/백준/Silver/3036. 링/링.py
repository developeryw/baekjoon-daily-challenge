import sys
input = sys.stdin.readline
from fractions import Fraction

N = int(input())
rings = list(map(int, input().split()))
first = rings[0]

result = []

for i in range(1, N):
    result.append(Fraction(rings[i], first))

for r in result:
    print(str(r.denominator) + "/" + str(r.numerator))
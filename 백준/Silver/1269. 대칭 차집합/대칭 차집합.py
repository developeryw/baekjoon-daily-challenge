import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

sym_dif = 0

def symmetric_difference(set_a, set_b):
    cnt = 0

    for element in set_a:
        if not element in set_b:
            cnt += 1

    return cnt

sym_dif += symmetric_difference(A, B)
sym_dif += symmetric_difference(B, A)

print(sym_dif)

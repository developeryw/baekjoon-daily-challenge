import sys
input = sys.stdin.readline

ss, kr, hy = map(int, input().split())
total = ss + kr + hy

if total >= 100:
    print("OK")
else:
    minimum = min(ss, kr, hy)
    if minimum == ss:
        print("Soongsil")
    elif minimum == kr:
        print("Korea")
    else:
        print("Hanyang")
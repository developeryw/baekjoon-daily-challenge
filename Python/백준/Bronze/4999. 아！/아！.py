import sys
input = sys.stdin.readline

jh = input().rstrip()
doctor = input().rstrip()

if len(jh) >= len(doctor):
    print("go")
else:
    print("no")
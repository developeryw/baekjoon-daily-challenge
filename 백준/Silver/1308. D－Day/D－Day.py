import sys
input = sys.stdin.readline
import datetime

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

dday = int(str(datetime.date(y2, m2, d2) - datetime.date(y1, m1, d1)).split()[0])

if y2 - y1> 1000:
    print("gg")
elif (y2 - y1 == 1000) and ((m2 > m1) or ((m2 == m1) and d2 >= d1)):
    print("gg")
else:
    print("D-" + str(dday))
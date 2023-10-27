import sys
from collections import deque
input = sys.stdin.readline

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

if angle1 == angle2 == angle3 == 60:
    print("Equilateral")
elif (angle1 == angle2 or angle2 == angle3 or angle3 == angle1) and (angle1 + angle2 + angle3 == 180):
    print("Isosceles")
elif angle1 != angle2 and angle2 != angle3 and angle3 != angle1 and (angle1 + angle2 + angle3 == 180):
    print("Scalene")
else:
    print("Error")
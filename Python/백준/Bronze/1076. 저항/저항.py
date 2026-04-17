import sys
input = sys.stdin.readline

resistance = {"black": [0, 1], "brown": [1, 10], "red": [2, 100], "orange": [3, 1000], "yellow": [4, 10000],
              "green": [5, 100000], "blue": [6, 1000000], "violet": [7, 10000000], "grey": [8, 100000000], "white": [9, 1000000000]}

first = input().rstrip()
second = input().rstrip()
third = input().rstrip()

input()

print((resistance[first][0] * 10 + resistance[second][0]) * resistance[third][1])
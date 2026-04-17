import sys
input = sys.stdin.readline

def switch(key):
    credit = {"A+": "4.3", "A0": "4.0", "A-": "3.7",
              "B+": "3.3", "B0": "3.0", "B-": "2.7",
              "C+": "2.3", "C0": "2.0", "C-": "1.7",
              "D+": "1.3", "D0": "1.0", "D-": "0.7",
              "F": "0.0"}

    return credit.get(score, "알 수 없음")

score = input().strip()

result = switch(score)
print(result)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
min_pack = 1000
min_per = 1000

for i in range(M):
    pack, per = map(int, input().split())

    min_pack = min(pack, min_pack)
    min_per = min(per, min_per)

minimum = min_pack * (N // 6) + min_per * (N % 6)
temp_min = min_pack * (N // 6 + 1)
temp_min2 = min_per * N

temp_min = min(temp_min2, temp_min)
minimum = min(temp_min, minimum)

print(minimum)
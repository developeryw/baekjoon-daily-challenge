import sys
input = sys.stdin.readline

heights = []

for i in range(9):
    tmp = int(input())
    heights.append(tmp)
    
for j in range(8):
    for k in range(j+1, 9):
        sum_of_7 = sum(heights) - (heights[j] + heights[k])
        
        if sum_of_7 == 100:
            heights.pop(j)
            heights.pop(k-1)
            heights.sort()
            print(*heights, sep='\n')
            exit(0)
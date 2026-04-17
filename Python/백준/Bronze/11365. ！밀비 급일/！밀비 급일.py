import sys
input = sys.stdin.readline

result = []

while True:
    letters = input().rstrip()
    
    if letters == 'END':
        print(*result, sep='\n')
        break
        
    result.append(letters[::-1])
        
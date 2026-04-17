import sys
input = sys.stdin.readline

lst = []

for _ in range(5):
    sock = int(input())
    
    if sock in lst:
        lst.pop(lst.index(sock))
    else:
        lst.append(sock)
        
print(*lst)
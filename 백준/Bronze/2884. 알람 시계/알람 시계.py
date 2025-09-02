import sys

input = sys.stdin.readline

h, m = map(int, input().split())

check_m = 0

check_m = m - 45

if check_m < 0:
    m = 60 + check_m
    if h == 0:
        h = 23
    else:
        h = h - 1
    
    print(f'{h} {m}')

elif check_m == 0:
    print(f'{h} {check_m}')

else:
    print(f'{h} {check_m}')

        
        






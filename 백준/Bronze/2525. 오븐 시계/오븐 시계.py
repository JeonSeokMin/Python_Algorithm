import sys

input = sys.stdin.readline

h, m = map(int, input().split())

cook = int(input())

check_m = 0
check_m = cook + m

m = check_m % 60

check_h = 0
check_h = check_m // 60

if h + check_h > 23:
    h = (h + check_h) - 24

else:
    h = h + check_h

print(f'{h} {m}')


        
        






import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

total = 0

if (a == b == c):
    total = 10000 + (a*1000)

elif (a == b != c):
    total = 1000 + (a*100)

elif (a == c != b):
    total = 1000 + (a*100)

elif (b == c != a):
    total = 1000 + (b*100)

else:
    total = max(a, b, c) * 100

print(total) 



        
        






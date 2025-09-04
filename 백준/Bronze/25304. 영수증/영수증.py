import sys

input = sys.stdin.readline

total = int(input())

n = int(input())

check_price = 0

for _ in range(n):
    price, count = map(int, input().split())

    check_price += (price * count)

if check_price == total:
    print("Yes")

else:
    print("No")
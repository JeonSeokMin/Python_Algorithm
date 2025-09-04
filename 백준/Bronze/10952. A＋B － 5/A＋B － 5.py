import sys

input = sys.stdin.readline

check_list = []

while True:

    a, b = map(int, input().split())

    if a == 0:
        break
    else:
        check_list.append((a, b))

for a, b in check_list:
    print(a + b)
import sys

input = sys.stdin.readline

check_list = []

while True:

    try:
        a, b = map(int, input().split())
        check_list.append((a, b))
    except:
        break

for a, b in check_list:
    print(a + b)
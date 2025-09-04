import sys

input = sys.stdin.readline

n = int(input())

check_list = []

for _ in range(n):
    a, b = map(int, input().split())
    check_list.append((a, b))

i = 1

for a, b in check_list:
    print(f'Case #{i}: {a} + {b} = {a+b}')
    i += 1
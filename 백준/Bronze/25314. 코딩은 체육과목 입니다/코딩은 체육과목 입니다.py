import sys

input = sys.stdin.readline

n = int(input())

check_number = n // 4

long_count = 'long ' * check_number

print(f'{long_count}int')
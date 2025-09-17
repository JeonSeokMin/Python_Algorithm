import sys

input = sys.stdin.readline

basic_chess = [1, 1, 2, 2, 2, 8]

now_chess = list(map(int, input().split()))

need_chess = []

for i in range(len(now_chess)):
    need_value = 0
    need_value = basic_chess[i] - now_chess[i]
    need_chess.append(need_value)

print(*need_chess)
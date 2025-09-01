import sys

input = sys.stdin.readline

a = input()
b = input()

total = 0
result_1 = 0
result_2 = 0
result_3 = 0

result_1 = int(a) * int(b[2])
print(result_1)

result_2 = int(a) * int(b[1])
print(result_2)

result_3 = int(a) * int(b[0])
print(result_3)

total = int(a)*int(b)
print(total)



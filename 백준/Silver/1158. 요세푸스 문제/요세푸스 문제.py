import sys

N, K = map(int, sys.stdin.readline().split())

people = []

for i in range(1, N+1):
    people.append(i)

startPoint = 0

answer = []

while people:
    startPoint = (startPoint + (K - 1)) % len(people)
    answer.append(people.pop(startPoint))

print("<" + ", ".join(map(str, answer)) + ">")
import sys

input = sys.stdin.readline

name = input()

name = name + "??!"

print(name.replace("\n", "")) # strip, 정규표현식 가능
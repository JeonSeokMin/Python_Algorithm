N = int(input())

heights = list(map(int, input().split()))
heights.sort()

answer = 0

left = [0]
right = [0]

for i in range(len(heights)):
    if heights[i] > max(left):
        left.append(heights[i])
    else:
        if heights[i] > max(right):
            right.append(heights[i])
        else:
            continue

answer = (len(left) - 1) + (len(right) - 1)

print(answer)


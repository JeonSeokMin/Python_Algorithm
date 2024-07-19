N, K = map(int, input().split())

room = list(map(int, input().split()))

room.append(0)

room.sort()

distance = []

for i in range(len(room)-1):
    
    distance.append(room[i+1] - room[i])

distance.sort()

result = 0
for i in range(len(distance) - K):
    result += distance[i]

print(result)
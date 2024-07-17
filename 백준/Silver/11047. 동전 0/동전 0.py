coin_Category, goal = map(int, input().split())

coins = []

for _ in range(coin_Category):
    coin = int(input())
    coins.append(coin)

# coins 리스트를 역순회 하면서 몫이 1보다 크거나 값은 코인에서 연산 시작
    
change = 0
answer = 0

for i in range(coin_Category-1, -1, -1):

    change = goal % coins[i]

    if change != goal:
        answer += (goal // coins[i])
        goal = change

print(answer)


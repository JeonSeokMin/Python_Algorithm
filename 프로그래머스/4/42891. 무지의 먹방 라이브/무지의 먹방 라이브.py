def solution(food_times, k):
    n = len(food_times)
    if sum(food_times) <= k:
        return -1

    foods = [(food, i+1) for i, food in enumerate(food_times)]
    foods.sort()
    pretime = 0
    for i, (food, idx) in enumerate(foods):
        diff = food - pretime
        if diff != 0:
            spend = diff * (n - i)
            if k >= spend:
                k -= spend
                pretime = food
            else:
                k %= (n - i)
                sublist = sorted(foods[i:], key=lambda x: x[1])
                return sublist[k][1]
    return -1
import math

N = int(input())

def is_Prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def dfs(n, m):
    if m == N:
        if is_Prime(n):
            print(n)
        return
    
    for i in range(1, 10):
        if i % 2 != 0 and is_Prime(n * 10 + i):
            dfs((n * 10) + i, m+1)

dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)





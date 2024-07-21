N, M = map(int, input().split())

visit = [0 for _ in range(N)]

adjust = [[] for _ in range(N)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    adjust[n1].append(n2)
    adjust[n2].append(n1)

arrive = False

def dfs(v, depth):

    global arrive
    
    if depth == 5 or arrive:
        arrive = True
        return
    
    visit[v] = 1
    for i in adjust[v]:
        if visit[i] == 0:
            dfs(i, depth+1)
        
    
    visit[v] = 0

for i in range(N):
    dfs(i, 1)

    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)

n = int(input())        # 사람 수

f1, f2 = map(int, input().split())      # 촌수 찾을 가족 수

m = int(input())

adjust = [[] for _ in range(n+1)]

visit = [0 for _ in range(n+1)]

find = False


for _ in range(m):
    n1, n2 = map(int, input().split())
    adjust[n1].append(n2)
    adjust[n2].append(n1)


def dfs(v, depth):

    global f2, find

    if v == f2:
        find = True
        print(depth)
    
    else:
        if visit[v] == 1:
            return
    
        else:
            visit[v] = 1

            for i in adjust[v]:
                if visit[i] == 0:
                    dfs(i, depth+1)
            
            visit[v] = 0            


dfs(f1, 0)
 
if not find:
    print("-1")
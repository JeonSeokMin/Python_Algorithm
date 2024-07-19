import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, E = map(int, input().split())

adjust = [[] for _ in range(N+1)]

for _ in range(E):
    n1, n2 = list(map(int, input().split()))
    adjust[n1].append(n2)
    adjust[n2].append(n1)



visit = [0 for _ in range(N+1)]



dfs_count = 0

def dfs(n):
    if visit[n] == 1:
        return
    else:
        visit[n] = 1
        for i in adjust[n]:
            if visit[i] == 0:
                dfs(i)

for i in range(1, N+1):
    if visit[i] == 0:
        dfs_count += 1
        dfs(i)

print(dfs_count)



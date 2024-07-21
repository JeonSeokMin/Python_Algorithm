from collections import deque


N, E, V = map(int, input().split())

adjust = [[] for _ in range(N + 1)]

# dfs 방문 배열
visit_dfs = [0 for _ in range(N+1)] 

# dfs 방문 순서
answer_dfs = []

# bfs 방분 배열
visit_bfs = [0 for _ in range(N+1)]

# bfs 활용 큐
bfs_queue = deque()

# bfs 방문 순서
answer_bfs = []

for _ in range(E):
    n1, n2 = map(int, input().split())
    adjust[n1].append(n2)
    adjust[n1].sort()
    adjust[n2].append(n1)
    adjust[n2].sort()

def dfs(v):
    if visit_dfs[v] == 1:
        return
    
    answer_dfs.append(v)

    visit_dfs[v] = 1    # 방문 처리

    for i in adjust[v]:
        dfs(i)

dfs(V)

for i in range(len(answer_dfs)):
    print(answer_dfs[i], end=' ')

print()

def bfs(v):

    bfs_queue.append(v)
    visit_bfs[v] = 1

    while(bfs_queue):

        temp = bfs_queue.popleft()
        print(temp, end=' ')

        for i in adjust[temp]:
            
            if visit_bfs[i] == 0:
                visit_bfs[i] = 1
                bfs_queue.append(i)

bfs(V)
        





# 1. while 큐가 빌때까지
# 2. start부터 시작해서 큐에 넣기
# 3. 하나씩 빼내면서 그와 연결된 인접리스트들을 큐에 넣으면서 visit배열 true로 변경
# 4. 출력








def solution(n, costs):
    
    costs.sort(key = lambda x:x[2])     # 비용을 기준으로 오름차순 정렬
    answer = 0
    link = set([costs[0][0]])       # 노드(섬)들의 연결 정보. 연결된 노드만 link 집합에 update
    
    while len(link) != n:
        for cost in costs:
            if cost[0] in link and cost[1] in link:     # 두 노드 모두 연결되어있다면
                continue        # 무시
            if cost[0] in link or cost[1] in link:    # 두 노드 중 연결되어있지 않은 경우
                link.update([cost[0], cost[1]])     # 연결되어있지 않은 노드 연결
                answer += cost[2]       # 연결비용 누적
                break
            
    return answer
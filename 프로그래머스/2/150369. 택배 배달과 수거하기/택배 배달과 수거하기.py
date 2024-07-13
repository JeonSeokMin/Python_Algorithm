def solution(cap, n, deliveries, pickups):
    
    answer = 0      # 거리 변수
    
    delivery = 0    # 몇 개를 배달하는지 카운트
    pickup = 0      # 몇 개를 수거하는지 카운트
    
    # 뒤에서부터 역순회 하면서 최대한 많이 배달하고 가져오기.
        
    for i in range(n-1, -1, -1):
        delivery += deliveries[i]   # 배달 상자 수 누적
        pickup += pickups[i]        # 수거 상자 수 누적
        
        while delivery > 0 or pickup > 0:       # 둘 중 하나라도 0보다 크다면 다시 돌아와서 수거해야한다는 뜻.
            delivery -= cap
            pickup -= cap
            answer += (i+1) * 2                 # 따라서 거리 * 2
        
        
    return answer
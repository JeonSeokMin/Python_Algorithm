def solution(n, lost, reserve):
    answer = 0
    lost.sort()     # 이건 몰랐네 lost 에 정렬 필요
    reserve.sort()  # reserve 에 정렬 필요
    check_lost = lost.copy()
    
    # 도난 당했지만 여벌 체육복을 챙겨온 경우
    for i in check_lost:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    
    check_lost = lost.copy()
    
    for i in check_lost:
        
        # 둘 다 있는 경우
        if i-1 in reserve and i+1 in reserve:
            print("있다1")
            lost.remove(i)
            reserve.remove(i-1)
            
        # 내 이전 사람만 여벌 체육복이 있는 경우
        elif i-1 in reserve and i+1 not in reserve:
            print("있다2")
            lost.remove(i)     # 체육복 빌림
            reserve.remove(i-1)    # 체육복 빌려줌
            
            
        # 내 이전 사람이 아닌 바로 뒤에 사람만 여벌 체육복이 있는 경우
        elif i-1 not in reserve and i+1 in reserve:
            print("있다3")
            lost.remove(i)     # 체육복 빌림
            reserve.remove(i+1)    # 체육복 빌려줌
        
        
        # 체육복을 빌리지 못하는 경우
        else:
            print("있다4")
            print(lost)
            continue

            
    answer = n - len(lost)
    return answer
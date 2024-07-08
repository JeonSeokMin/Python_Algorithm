def solution(people, limit):
    people.sort()
    answer = 0
    
    start = 0   # 몸무게가 가장 작은 사람의 인덱스(리스트의 왼쪽)
    end = len(people) - 1   # 몸무게가 가장 많은 사람의 인덱스(리스트의 오른쪽)
    
    while(True):
        if start < end: 
            if people[start] + people[end] <= limit:
                answer += 1     # 두 명을 태울 보트 하나
                start += 1      # 몸무게 작은 사람 탑승
                end -= 1        # 몸무게 많은 사람 탑승

            else:
                answer += 1     # 몸무게 많은 사람만 태울 보트 하나
                end -= 1        # 몸무게 많은 사람 탑승
            
        elif start == end:
            answer += 1
            break
        else:
            break
            
    return answer
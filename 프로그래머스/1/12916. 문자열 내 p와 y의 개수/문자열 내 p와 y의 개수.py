def solution(s):
    answer = True
    
    cnt_p = 0
    cnt_y = 0
    
    for i in s:
        if i == 'p' or i == 'P':
            cnt_p += 1
        elif i == 'y' or i == 'Y':
            cnt_y += 1
        else:
            continue
            
    if cnt_p == cnt_y:
        answer = True
    else:
        answer = False
    
    
    
 

    return answer
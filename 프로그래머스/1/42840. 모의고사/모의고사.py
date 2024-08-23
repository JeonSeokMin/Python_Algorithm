def solution(answers):
    
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = []
    
    correct_answer_1 = 0
    correct_answer_2 = 0
    correct_answer_3 = 0
    
    for i in range(len(answers)):
        if list_1[i % len(list_1)] == answers[i]:
            correct_answer_1 += 1
        
        if list_2[i % len(list_2)] == answers[i]:
            correct_answer_2 += 1
            
        
        if list_3[i % len(list_3)] == answers[i]:
            correct_answer_3 += 1
        
    max_value = max(correct_answer_1, correct_answer_2, correct_answer_3)
    
    if correct_answer_1 == max_value:
        answer.append(1)

    if correct_answer_2 == max_value:
        answer.append(2)

    if correct_answer_3 == max_value:
        answer.append(3)
    
    answer.sort()
    
    return answer
def solution(sizes):
    
    width = []
    height = []
    
    for i in sizes:
        width.append(max(i))
        height.append(min(i))
        
    
    answer = max(width) * max(height)
    return answer
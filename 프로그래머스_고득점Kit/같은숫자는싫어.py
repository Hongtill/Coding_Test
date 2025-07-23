from collections import deque

def solution(arr):
    answer = []
    
    for i in arr :
        if len(answer) == 0 :
            answer.append(i)
        else :
            elem = answer.pop()
            answer.append(elem)
            
            if elem == i :
                continue
            else :
                answer.append(i)
                
    return answer


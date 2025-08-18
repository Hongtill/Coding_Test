def solution(progresses, speeds):
    answer = []
    temp = []
    temp_2 = []
    
    for i in range(len(progresses)) :
        
        if (100 - progresses[i]) % speeds[i] == 0 :
            count = int((100 - progresses[i]) / speeds[i])
        else :
            count = int((100 - progresses[i]) / speeds[i]) + 1
            
        temp.append(count)
            
    for i in range(len(temp)) :
        if len(answer) == 0 :
            answer.append(1)
            temp_2.append(temp[i])
        else :
            if temp_2[-1] >= temp[i] :
                top_elem = answer.pop()
                answer.append(top_elem+1)
            else :
                answer.append(1)
                temp_2.append(temp[i])
            

    
    return answer

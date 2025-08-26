from itertools import permutations

def solution(numbers):
    answer = ''
    
    new_numbers = list(permutations(numbers, len(numbers)))
    
    temp_list = []
    
    for i in range(len(new_numbers)) :
        answer = ''
        
        for j in range(len(numbers)) :
            answer = answer + str(new_numbers[i][j])
            
        answer = int(answer)
        temp_list.append(answer)
    
    temp_list.sort()
    
    answer = str(temp_list[-1])
    
    
    return answer
